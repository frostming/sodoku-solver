import sys

from sodoku_solver.generate import generate
from sodoku_solver.problem import new_problem
from sodoku_solver.solution import solution


def main():
    cmd = sys.argv[1]
    if cmd == "generate":
        generate()
    elif cmd == "new":
        new_problem()
    elif cmd == "solution":
        solution()


if __name__ == "__main__":
    main()
