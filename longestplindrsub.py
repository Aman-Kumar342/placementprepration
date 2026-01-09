import sys


def is_palind(s):
    return s == s[::-1]


def longest_palind(s):
    if not s:
        return ""
    best = ""
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if len(sub) > len(best) and is_palind(sub):
                best = sub
    return best


def main():
    text = sys.stdin.read()
    if not text:
        return
    s = text.rstrip("\n")
    print(longest_palind(s))


if __name__ == "__main__":
    main()
