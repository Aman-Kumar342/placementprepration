import sys

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def is_balanced(root):
    def height(node):
        if not node:
            return 0, True
        lh, lb = height(node.left)
        rh, rb = height(node.right)
        balanced = lb and rb and abs(lh - rh) <= 1
        return max(lh, rh) + 1, balanced
    return height(root)[1]


def main():
    # Placeholder tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print("The tree is balanced." if is_balanced(root) else "The tree is NOT balanced.")


if __name__ == "__main__":
    main()
