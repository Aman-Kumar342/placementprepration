import sys


def is_armstrong(num):
    # Computes whether a number equals the sum of its digits raised to the digit count
    digits = list(map(int, str(abs(num))))
    power = len(digits)
    return num == sum(d ** power for d in digits)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    if is_armstrong(n):
        print("It is a armstrong ")
    else:
        print("Not a")


if __name__ == "__main__":
    main()
