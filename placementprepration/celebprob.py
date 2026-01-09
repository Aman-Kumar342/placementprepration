import sys


def knows(matrix, a, b):
    return matrix[a][b] == 1


def find_celeb(matrix):
    n = len(matrix)
    stack = list(range(n))
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if knows(matrix, a, b):
            stack.append(b)
        else:
            stack.append(a)
    cand = stack.pop()
    for i in range(n):
        if i == cand:
            continue
        if knows(cand_matrix := matrix, cand, i) or not knows(cand_matrix, i, cand):
            return -1
    return cand


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    vals = rest[: n * n]
    matrix = [vals[i * n : (i + 1) * n] for i in range(n)]
    celeb = find_celeb(matrix)
    if celeb == -1:
        print("No celebrirt")
    else:
        print(celeb)


if __name__ == "__main__":
    main()
