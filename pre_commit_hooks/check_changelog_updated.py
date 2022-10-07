from __future__ import annotations

import argparse
import logging
from typing import Sequence

from pre_commit_hooks.util import cmd_output

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")


def main(argv: Sequence[str] | None = None) -> int:
    """Check if the changelog has been updated."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", default="CHANGELOG.md", nargs="?")
    args = parser.parse_args(argv)

    try:
        git_origin = cmd_output("git", "remote", "show", "origin")
        default_branch = git_origin.split("HEAD branch: ")[1].splitlines()[0]
        git_diff = cmd_output(
            "git",
            "diff",
            f"origin/{default_branch}",
            "--",
            args.filename,
        )
        if git_diff:
            logger.info(f"'{args.filename}' has been updated.")
            return 0
    except Exception as exc:
        logger.debug("Failed to retrieve git status", exc_info=exc)
        return 1
    else:
        logger.info(f"'{args.filename}' not updated")
        return 1


if __name__ == "__main__":
    SystemExit(main())
