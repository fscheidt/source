import os
import fnmatch
from pathlib import Path
from rich import print


def search_files(
    folderpath: Path,
    extensions: list = ["*"],
    ignore_extensions: list = None,
    max_files: int = 0,
    ignore_parts: list[str] = [],
    keywords: str = None,
    sort_files: bool = True,
    verbose: bool = None,
) -> list[Path]:
    """
    Search for files in the filesystem given a folder and criteria
    """
    ignore_extensions = ignore_extensions or []
    ignore_parts = ignore_parts or []
    files = []
    for root, _, filenames in os.walk(folderpath):
        for ext in extensions:
            for filename in fnmatch.filter(filenames, ext):
                fp = Path(os.path.join(root, filename))
                if len(ignore_extensions) > 0 and fp.suffix in ignore_extensions:
                    continue
                if any(part in fp.parts for part in ignore_parts):
                    continue
                if keywords:
                    content = fp.read_text(encoding="utf-8", errors="ignore")
                    if keywords not in content:
                        continue
                files.append(fp)
    files = sorted(files, key=lambda f: str(f)) if sort_files else files
    if max_files > 0 and len(files) > max_files:
        files = files[:max_files]
    if verbose:
        print(locals())
        print(f"found={len(files)}")
    return files
