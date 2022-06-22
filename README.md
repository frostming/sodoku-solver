# Package Manager Sodoku Solver

The original work: https://github.com/mildbyte/poetry-sudoku-solver/
The article: https://www.splitgraph.com/blog/poetry-dependency-resolver-sudoku

## Usage

1. Install the depenendencies([PDM](https://github.com/pdm-project/pdm) is required).

   ```bash
   pdm install
   ```

2. Generate dummy packages and start the local PyPI server:

   ```bash
   pdm run pypi
   ```

3. Visit https://qqwing.com/generate.html to generate a Sudoku puzzle. Paste it into `puzzle.txt`
4. Solve the Sodoku with specified package manager.

   ```bash
   pdm run puzzle [pdm|pipenv|poetry]
   ```

   You need to have the called package manager installed and discoverable in `PATH`.
