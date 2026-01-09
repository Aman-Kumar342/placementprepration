import sys

def stock_span(prices):
    stack = []
    spans = []
    for price in prices:
        span = 1
        while stack and stack[-1][0] <= price:
            span += stack.pop()[1]
        stack.append((price, span))
        spans.append(span)
    return spans


def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n, *rest = data
    prices = rest[:n]
    res = stock_span(prices)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
