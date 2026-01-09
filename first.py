import sys


def main():
    print("1.println")
    print("2.println")
    number = -10.6
    print("I am  awesome")
    print(f"number={number}")
    a, b = 3, 4
    print(a + b)
    print("3" + "4")
    print(str(a + b))
    print(f"{3 + 4 + a} {b}{a}")
    print("Result: " + str(a) + str(b))
    print(f"Result: {a + b}")
    ch = chr(85)
    ch1 = 'A'
    print(ch)
    print(ch1)

    tokens = sys.stdin.read().splitlines()
    if not tokens:
        return
    s = tokens[0]
    print("your string is " + s)
    ints = []
    for line in tokens[1:]:
        for part in line.split():
            try:
                ints.append(int(part))
            except ValueError:
                pass
    labels = ["your number is ", "your numbr is ", "your number is "]
    for label, value in zip(labels, ints):
        print(label + str(value))


if __name__ == "__main__":
    main()
