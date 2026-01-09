import sys

def is_stack_permutation(inp, out):
    if len(inp) != len(out):
        return False
    stack = []
    j = 0
    for val in inp:
        stack.append(val)
        while stack and j < len(out) and stack[-1] == out[j]:
            stack.pop()
            j += 1
    return not stack


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    inp = [int(next(it)) for _ in range(n)]
    m = int(next(it, n))
    out = [int(next(it)) for _ in range(m)]
    if is_stack_permutation(inp, out):
        print("Yes the 2nd array is permutation of the first array")
    else:
        print("No the array is not the permutaion of the first array")


if __name__ == "__main__":
    main()
