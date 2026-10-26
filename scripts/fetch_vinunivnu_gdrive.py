"""Resumable, striped downloader for the vinunivnu (Task 3) Google Drive archive.

Usage: python scripts/fetch_vinunivnu_gdrive.py [dest_dir]

The submission is a 3.1 GB tar.gz (OCI/Docker image export) hosted on Google
Drive.  A single connection is throttled to roughly 0.3 MB/s on this link, so
the transfer is split into stripes that are fetched concurrently and then
concatenated.  Every stripe resumes from whatever it already downloaded.
"""

from __future__ import annotations

import os
import sys
import threading
import time
import urllib.request

FILE_ID = "1xFapoEOu8BOPA6b9mE0qQ37X9KjOJbCv"
URL = f"https://drive.usercontent.google.com/download?id={FILE_ID}&export=download&confirm=t"
TOTAL = 3_363_717_233  # bytes, from the Content-Range header
NSTRIPES = 8
CHUNK = 4 << 20

dest_dir = ""
lock = threading.Lock()
progress = {"bytes": 0}


def stripe_bounds(index: int) -> tuple[int, int]:
    span = TOTAL // NSTRIPES
    start = index * span
    end = TOTAL - 1 if index == NSTRIPES - 1 else (index + 1) * span - 1
    return start, end


def fetch_stripe(index: int) -> None:
    start, end = stripe_bounds(index)
    path = os.path.join(dest_dir, f"part{index}.bin")
    attempt = 0
    while True:
        have = os.path.getsize(path) if os.path.exists(path) else 0
        if start + have > end:
            return
        attempt += 1
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Range": f"bytes={start + have}-{end}",
        }
        try:
            req = urllib.request.Request(URL, headers=headers)
            with urllib.request.urlopen(req, timeout=180) as resp:
                if resp.status != 206:
                    raise RuntimeError(f"unexpected status {resp.status}")
                with open(path, "ab") as fh:
                    while True:
                        chunk = resp.read(CHUNK)
                        if not chunk:
                            break
                        fh.write(chunk)
                        have += len(chunk)
                        with lock:
                            progress["bytes"] += len(chunk)
        except Exception as exc:  # noqa: BLE001 - retry any transport error
            print(f"stripe {index} attempt {attempt} stopped: {exc!r}", flush=True)
            if attempt >= 300:
                raise
            time.sleep(min(10 * attempt, 60))


def main() -> int:
    global dest_dir
    dest_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.environ["TEMP"], "vinunivnu")
    os.makedirs(dest_dir, exist_ok=True)
    for name in os.listdir(dest_dir):
        if name.startswith("part") and name.endswith(".bin"):
            with lock:
                progress["bytes"] += os.path.getsize(os.path.join(dest_dir, name))

    threads = [threading.Thread(target=fetch_stripe, args=(i,), daemon=True) for i in range(NSTRIPES)]
    for t in threads:
        t.start()

    started = time.time()
    while any(t.is_alive() for t in threads):
        time.sleep(30)
        with lock:
            done = progress["bytes"]
        rate = done / 1e6 / max(time.time() - started, 1e-6)
        print(
            f"progress {done/1e9:.3f}/{TOTAL/1e9:.3f} GB ({100*done/TOTAL:.1f}%) "
            f"session avg {rate:.2f} MB/s",
            flush=True,
        )
    for t in threads:
        t.join()

    final = os.path.join(dest_dir, "vinunivnu.tar.gz")
    with open(final, "wb") as out:
        for i in range(NSTRIPES):
            with open(os.path.join(dest_dir, f"part{i}.bin"), "rb") as src:
                while True:
                    buf = src.read(16 << 20)
                    if not buf:
                        break
                    out.write(buf)
    size = os.path.getsize(final)
    print(f"done: {final} ({size} bytes, expected {TOTAL})", flush=True)
    return 0 if size == TOTAL else 1


if __name__ == "__main__":
    raise SystemExit(main())
