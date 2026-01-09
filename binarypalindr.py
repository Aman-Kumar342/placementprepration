import sys


def is_binary_palindrome(n):
    b = bin(n)[2:]
    return b == b[::-1]


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    if is_binary_palindrome(n):
        print("it is a palindrom")
    else:
        print("It sis not a palindrome")


if __name__ == "__main__":
    main()
