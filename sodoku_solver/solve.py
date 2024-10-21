import json
import os
import subprocess
import sys
import time
from typing import List

import tomli

from sodoku_solver.consts import OUTPUT_DIR


def parse_solution(lockfile: str) -> str:
    if os.path.basename(lockfile) == "Pipfile.lock":
        with open(lockfile, "rb") as f:
            data = json.load(f)

        cell_values = {
            (int(name[-2]), int(name[-1])): int(value["version"][2:])
            for name, value in data["default"].items()
        }
    elif os.path.basename(lockfile) == "pip.lock":
        with open(lockfile, "rb") as f:
            data = json.load(f)

        cell_values = {
            (int((name := p["metadata"]["name"])[-2]), int(name[-1])): int(
                p["metadata"]["version"]
            )
            for p in data["install"]
        }
    else:
        with open(lockfile, "rb") as f:
            data = tomli.load(f)

        cell_values = {
            (int(p["name"][-2]), int(p["name"][-1])): int(p["version"][0])
            for p in data["package"]
            if p["name"][-2:].isdigit()
        }

    lines: List[str] = []
    for row in range(1, 10):
        if row in (4, 7):
            lines.append("-------|-------|-------")
        line = " "
        for col in range(1, 10):
            if col in (4, 7):
                line += "| "
            line += f"{cell_values[row, col]} "
        lines.append(line)
    return "\n".join(lines)


def solve(package_manager: str) -> str:
    project = OUTPUT_DIR / f"{package_manager}-project"

    if package_manager == "pip":
        args = [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt",
            "--dry-run",
            "--report",
            "pip.lock",
        ]
    else:
        args = [package_manager, "lock"]

    start = time.monotonic()
    subprocess.check_call(args, cwd=str(project))
    elapse = time.monotonic() - start
    print(
        f"\n============ Time Cost ============\n"
        f"  {package_manager} took {elapse:.2f} seconds"
    )
    lockfile = project.joinpath(
        "Pipfile.lock" if package_manager == "pipenv" else f"{package_manager}.lock"
    )
    print("\n============ Solution ============")
    print(parse_solution(lockfile))
