import sys


def toh(n, src, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return
    toh(n - 1, src, dest, aux)
    print(f"Move disk {n} from {src} to {dest}")
    toh(n - 1, aux, src, dest)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    toh(n, 'a', 'b', 'c')


if __name__ == "__main__":
    main()
