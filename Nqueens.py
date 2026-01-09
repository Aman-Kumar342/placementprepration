import sys


def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def place_queens(board, row, out_lines):
    n = len(board)
    if row == n:
        for r in board:
            out_lines.append("." * r + "Q" + "." * (n - r - 1))
        out_lines.append("")
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            place_queens(board, row + 1, out_lines)


def solve(n):
    board = [-1] * n
    lines = []
    place_queens(board, 0, lines)
    return lines


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    for line in solve(n):
        print(line)


if __name__ == "__main__":
    main()
