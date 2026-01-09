import sys

def swap_chars(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return "".join(lst)


def permute(s, left, right, out):
    if left == right:
        out.append(s)
    else:
        for i in range(left, right + 1):
            s = swap_chars(s, left, i)
            permute(s, left + 1, right, out)
            s = swap_chars(s, left, i)


def main():
    s = sys.stdin.read().strip("\n")
    if not s:
        return
    out = []
    permute(s, 0, len(s) - 1, out)
    for p in out:
        print(p)


if __name__ == "__main__":
    main()
