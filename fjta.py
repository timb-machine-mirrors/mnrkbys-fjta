#!/usr/bin/env python3
#
# fjta.py
# Forensic Journal Timeline Analyzer (FJTA) can parse and analyze journal log of ext4 and XFS file systems.
#
# Copyright 2025 Minoru Kobayashi <unknownbit@gmail.com> (@unkn0wnbit)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import argparse
import sys

from journalparser import journalparser
from journalparser.version import VERSION


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a timeline of file system activities from the filesystem journal log.",
    )
    parser.add_argument(
        "-i",
        "--image",
        type=str,
        help="Path to a disk image file.",
    )
    parser.add_argument(
        "-s",
        "--offset",
        type=int,
        default=0,
        help="Filesystem offset in bytes. (Default: 0)",
    )
    # parser.add_argument(
    #     "-o",
    #     "--output",
    #     type=str,
    #     help="Path to an output file. (Default: stdout)",
    # )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode. (Default: False)",
    )
    parser.add_argument(
        "--special-inodes",
        action="store_true",
        help="Include special inodes in the timeline. (Default: False)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    return parser.parse_args()

def main() -> None:
    if not args.image:
        print("Please specify a disk image file.", file=sys.stderr)
        sys.exit(1)

    parser = journalparser.JournalParser(args.image, args)
    parser.parse_journal()
    parser.timeline()


if __name__ == "__main__":
    args = parse_arguments()
    main()
