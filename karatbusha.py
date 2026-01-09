import sys


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(abs(x))), len(str(abs(y))))
    half = n // 2
    power = 10 ** half
    a, b = divmod(x, power)
    c, d = divmod(y, power)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + ad_plus_bc * power + bd


def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    x, y = map(int, data[:2])
    print(karatsuba(x, y))


if __name__ == "__main__":
    main()
