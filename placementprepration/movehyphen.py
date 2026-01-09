import sys


def move_hyphen_to_beginning(text):
    if text is None or "-" not in text:
        return text
    return "-" + text.replace("-", "")


def main():
    s = sys.stdin.read()
    if not s:
        return
    s = s.rstrip("\n")
    print(move_hyphen_to_beginning(s))


if __name__ == "__main__":
    main()
