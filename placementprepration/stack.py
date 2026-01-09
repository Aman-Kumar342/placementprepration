class Stack:
    def __init__(self, size):
        self.max_size = size
        self.array = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, value):
        if self.is_full():
            return None
        self.top += 1
        self.array[self.top] = value
        return value

    def pop(self):
        if self.is_empty():
            return None
        value = self.array[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.top]


if __name__ == "__main__":
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element is:", s.peek())
    print(s.pop(), "popped from stack")
    print(s.pop(), "popped from stack")
    print("Is stack empty?", "Yes" if s.is_empty() else "No")
