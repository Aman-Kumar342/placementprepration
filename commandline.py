import sys


def main():
    if len(sys.argv) < 3:
        return
    # Mimics Java string concatenation of first two CLI args
    print(sys.argv[1] + sys.argv[2])


if __name__ == "__main__":
    main()
