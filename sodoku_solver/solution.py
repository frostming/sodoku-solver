import sys
from typing import List

import tomli


def parse_solution(lockfile: str) -> str:
    with open(lockfile, "rb") as f:
        data = tomli.load(f)

    cell_values = {
        (int(p["name"][-2]), int(p["name"][-1])): int(p["version"][0])
        for p in data["package"]
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


def solution():
    print(parse_solution(sys.argv[-1]))
