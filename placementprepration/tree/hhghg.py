# Simple recursive-descent parser demo for grammar S->0S1|01
import sys
sys.setrecursionlimit(10000)


class Parser:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def parse_S(self):
        if self.i < len(self.s) and self.s[self.i] == '0':
            self.i += 1
            if self.i < len(self.s) and self.s[self.i] == '1':
                self.i += 1
                return True
            if self.parse_S() and self.i < len(self.s) and self.s[self.i] == '1':
                self.i += 1
                return True
        return False

    def parse(self):
        ok = self.parse_S()
        return ok and self.i == len(self.s)


def check(s):
    return Parser(s).parse()


if __name__ == "__main__":
    for test in ["01", "0011", "000111", "011", "0", ""]:
        print(test, check(test))
