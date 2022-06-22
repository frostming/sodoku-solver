import sys


from .generate import generate


def main():
    cmd = sys.argv[1]
    if cmd == "generate":
        generate()


if __name__ == "__main__":
    main()
