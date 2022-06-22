import sys

from sodoku_solver.generate import generate
from sodoku_solver.problem import new_problem
from sodoku_solver.solve import solve


def main():
    cmd = sys.argv[1]
    if cmd == "generate":
        generate()
    elif cmd == "new":
        new_problem(sys.argv[2], sys.argv[3])
    elif cmd == "solve":
        solve(sys.argv[2])
    elif cmd == "puzzle":
        new_problem(sys.argv[2], "puzzle.txt")
        solve(sys.argv[2])
    else:
        sys.exit("unknown command, accepted commands: generate, new, solve, puzzle")


if __name__ == "__main__":
    main()
