import sys


def main():
    if len(sys.argv) < 3:
        return
    print(sys.argv[1] + sys.argv[2])


if __name__ == "__main__":
    main()
