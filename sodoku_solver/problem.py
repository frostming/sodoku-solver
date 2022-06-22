import sys
from typing import Iterable, List
from sodoku_solver.consts import OUTPUT_DIR


def _get_dependencies(lines: Iterable[str]) -> List[str]:
    i = 1
    result: List[str] = []

    for line in lines:
        j = 1
        line = line.strip()
        if not line:
            break
        if line[0] == "-":
            continue
        for c in line:
            if not c.strip() or c == "|":
                continue
            if c == ".":
                result.append(f"sodoku-cell{i}{j}")
            else:
                result.append(f"sodoku-cell{i}{j}=={c}")
            j += 1
        i += 1

    return result


TEMPLATE = """\
[project]
name = ""
version = ""
dependencies = {!r}
requires-python = ">=3.8"

[[tool.pdm.source]]
name = "pypi"
url = "http://localhost:8080/simple/"
verify_ssl = false
"""


def new_problem() -> None:
    filename = sys.argv[-1]
    with open(filename, "r") as f:
        dependencies = _get_dependencies(f)

    content = TEMPLATE.format(dependencies)
    OUTPUT_DIR.joinpath("test-project").mkdir(exist_ok=True)
    OUTPUT_DIR.joinpath("test-project", "pyproject.toml").write_text(content)
