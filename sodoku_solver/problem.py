from typing import Iterable, List, Tuple

from sodoku_solver.consts import OUTPUT_DIR
from sodoku_solver.templates import TEMPLATES


def _get_dependencies(lines: Iterable[str]) -> List[Tuple[str, str]]:
    i = 1
    result: List[Tuple[str, str]] = []

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
                version = ""
            else:
                version = str(c)
            result.append((f"sodoku-cell{i}{j}", version))
            j += 1
        i += 1

    return sorted(result)


def new_problem(package_manager: str, filename: str) -> None:
    with open(filename, "r") as f:
        dependencies = _get_dependencies(f)

    template = TEMPLATES[package_manager]
    content = template(dependencies)
    OUTPUT_DIR.joinpath(f"{package_manager}-project").mkdir(exist_ok=True)
    project_file = (
        "Pipfile"
        if package_manager == "pipenv"
        else "requirements.txt"
        if package_manager == "pip"
        else "pyproject.toml"
    )
    OUTPUT_DIR.joinpath(f"{package_manager}-project", project_file).write_text(content)
