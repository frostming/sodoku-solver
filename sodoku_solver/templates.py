import json
from typing import Iterable, List, Tuple


PEP621_TEMPLATE = """\
[project]
name = ""
version = ""
dependencies = {}
requires-python = ">=3.8"

[[tool.pdm.source]]
name = "pypi"
url = "http://localhost:8080/simple/"
verify_ssl = false
"""

POETRY_TEMPLATE = """\
[tool.poetry]
name = "poetry-project"
version = "0.1.0"
description = ""
authors = ["John Doe <john@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
{}

[[tool.poetry.source]]
name = "local"
url = "http://localhost:8080/simple/"
default = true
"""

PIPFILE_TEMPLATE = """
[packages]
{}

[[source]]
name = "pypi"
url = "http://localhost:8080/simple/"
verify_ssl = false
"""


def fill_pep621(dependencies: Iterable[Tuple[str, str]]) -> str:
    dependency_array = [
        f"{name}=={version}" if version else name for name, version in dependencies
    ]
    return PEP621_TEMPLATE.format(json.dumps(dependency_array, indent=2))


def fill_poetry(dependencies: Iterable[Tuple[str, str]]) -> str:
    lines: List[str] = []
    for name, version in dependencies:
        if version:
            line = f'{name} = "{version}"'
        else:
            line = f'{name} = "*"'
        lines.append(line)
    return POETRY_TEMPLATE.format("\n".join(lines))


def fill_pipenv(dependencies: Iterable[Tuple[str, str]]) -> str:
    lines: List[str] = []
    for name, version in dependencies:
        if version:
            line = f'{name} = "=={version}"'
        else:
            line = f'{name} = "*"'
        lines.append(line)
    return PIPFILE_TEMPLATE.format("\n".join(lines))


TEMPLATES = {"pdm": fill_pep621, "poetry": fill_poetry, "pipenv": fill_pipenv}
