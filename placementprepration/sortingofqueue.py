import sys
from collections import deque


def sort_queue(queue_vals):
    sorted_vals = sorted(queue_vals)
    return deque(sorted_vals)


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    vals = rest[:n]
    sorted_q = sort_queue(vals)
    print(f"ans :{list(sorted_q)}")


if __name__ == "__main__":
    main()
