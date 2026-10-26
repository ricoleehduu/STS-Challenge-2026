"""Inspect / extract source code from the vinunivnu OCI image archive.

Usage:
    python scripts/extract_oci_code.py list    <archive.tar.gz>
    python scripts/extract_oci_code.py extract <archive.tar.gz> <out_dir> [path_prefix]

The archive is an OCI/Docker image export: `blobs/sha256/<digest>` files, most
of them gzip-compressed layer tars.  Layer tars are streamed and only files that
look like source code are considered; base-image trees (conda, site-packages,
apt state, ...) and binary weights are skipped.
"""

from __future__ import annotations

import collections
import gzip
import os
import sys
import tarfile

CODE_EXT = {
    ".py", ".sh", ".bash", ".yaml", ".yml", ".json", ".md", ".txt", ".cfg", ".toml",
    ".ini", ".ipynb", ".c", ".cc", ".cpp", ".cu", ".h", ".hpp", ".java", ".js", ".ts",
    ".sql", ".dockerfile", ".env", ".in", ".template", ".patch", ".diff", ".csv",
}
CODE_NAMES = {
    "dockerfile", "makefile", "license", "readme", "requirements.txt", "environment.yml",
    "setup.py", "pyproject.toml", "run.sh", "predict.sh", "train.sh", "entrypoint.sh",
    ".gitattributes", ".gitignore", ".dockerignore",
}
SKIP_PARTS = {
    "site-packages", "dist-packages", "node_modules", "__pycache__", ".cache", ".git",
    "conda-meta", "pkgs", "opt/conda", "usr/lib", "usr/share", "usr/include", "var/lib",
    ".conda", "dist-info", "egg-info",
}
SKIP_PREFIXES = ("opt/conda", "usr/", "var/", "etc/", "lib/", "bin/", "sbin/", "boot/", "proc/", "sys/")
MAX_FILE = 5 << 20  # ignore anything larger than 5 MB


def wanted(name: str, size: int) -> bool:
    if size == 0 or size > MAX_FILE:
        return False
    if name.startswith(SKIP_PREFIXES):
        return False
    low = name.lower()
    if any(part in low for part in SKIP_PARTS):
        return False
    base = os.path.basename(low)
    ext = os.path.splitext(base)[1]
    if base in CODE_NAMES or ext in CODE_EXT:
        return True
    return ext == "" and "/" in name  # extension-less scripts inside a project tree


def layers(archive: str):
    """Yield (blob_name, inner tar stream) for every layer blob, in tar order."""
    with tarfile.open(archive, "r:gz") as outer:
        for member in outer:
            if not member.isfile() or "blobs/sha256/" not in member.name:
                continue
            fh = outer.extractfile(member)
            head = fh.read(512)
            fh.seek(0)
            if head[:2] == b"\x1f\x8b":
                fh = gzip.GzipFile(fileobj=fh)
            elif head[257:262] != b"ustar":
                continue  # config / manifest blob
            yield member.name, tarfile.open(fileobj=fh, mode="r|")


def cmd_list(archive: str) -> int:
    for blob, inner in layers(archive):
        dirs: collections.Counter[str] = collections.Counter()
        total = kept = 0
        try:
            with inner:
                for m in inner:
                    if not m.isfile():
                        continue
                    total += 1
                    if wanted(m.name.lstrip("./"), m.size):
                        kept += 1
                        parts = m.name.lstrip("./").split("/")
                        dirs["/".join(parts[:2]) if len(parts) > 1 else "."] += 1
        except Exception as exc:  # noqa: BLE001 - truncated/partial archive
            print(f"  [stop early: {exc!r}]")
        print(f"== {blob}  files={total} code_like={kept}")
        for d, c in dirs.most_common(15):
            print(f"   {c:5d}  {d}")
    return 0


def cmd_extract(archive: str, out_dir: str, prefix: str | None) -> int:
    written = 0
    for blob, inner in layers(archive):
        try:
            with inner:
                for m in inner:
                    if not m.isfile():
                        continue
                    name = m.name.lstrip("./")
                    if prefix and not name.startswith(prefix):
                        continue
                    if not wanted(name, m.size):
                        continue
                    dest = os.path.join(out_dir, name)
                    os.makedirs(os.path.dirname(dest), exist_ok=True)
                    src = inner.extractfile(m)
                    if src is None:
                        continue
                    if os.path.exists(dest) and os.path.getsize(dest) == m.size:
                        continue
                    with open(dest, "wb") as out:
                        while True:
                            buf = src.read(1 << 20)
                            if not buf:
                                break
                            out.write(buf)
                    written += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  [stop early on {blob}: {exc!r}]")
    print(f"extracted {written} files into {out_dir}")
    return 0


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    cmd, archive = sys.argv[1], sys.argv[2]
    if cmd == "list":
        return cmd_list(archive)
    if cmd == "extract":
        prefix = sys.argv[4] if len(sys.argv) > 4 else None
        return cmd_extract(archive, sys.argv[3], prefix)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
