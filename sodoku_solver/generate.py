from typing import List, Set

from pdm.pep517.wheel import WheelBuilder

from sodoku_solver.consts import OUTPUT_DIR, TEMPLATE_PATH

RANGE = range(9)


def _calculate_dependencies(row: int, col: int, version: int) -> List[str]:
    result: Set[str] = set()
    for i in RANGE:
        for j in RANGE:
            if i == row and j == col:
                continue
            if i == row:
                result.add(f"sodoku-cell{i+1}{j+1}!={version}")
            elif j == col:
                result.add(f"sodoku-cell{i+1}{j+1}!={version}")
            elif (i // 3) == (row // 3) and (j // 3) == (col // 3):
                result.add(f"sodoku-cell{i+1}{j+1}!={version}")
    return sorted(result)


def generate_package(row: int, col: int, version: int) -> None:
    print(f"generating package for sodoku-cell{row+1}{col+1}=={version}")
    with WheelBuilder(TEMPLATE_PATH) as builder:
        meta = builder.meta
        meta._metadata["name"] = f"sodoku-cell{row+1}{col+1}"
        meta._metadata["version"] = str(version)
        meta._metadata["dependencies"] = _calculate_dependencies(row, col, version)
        builder.build(OUTPUT_DIR / "packages")


def generate():
    OUTPUT_DIR.joinpath("packages").mkdir()
    for row in RANGE:
        for col in RANGE:
            for version in range(1, 10):
                generate_package(row, col, version)
