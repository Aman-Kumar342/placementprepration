def find_x(num1, rem1, num2, rem2):
    x = 1
    while True:
        if x % num1 == rem1 and x % num2 == rem2:
            return x
        x += 1


def main():
    num1, rem1 = 7, 2
    num2, rem2 = 11, 3
    x = find_x(num1, rem1, num2, rem2)
    print(f"The smallest x satisfying the given congruences is: {x}")


if __name__ == "__main__":
    main()
