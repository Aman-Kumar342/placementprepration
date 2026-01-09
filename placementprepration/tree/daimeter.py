class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def diameter(root):
    max_dia = 0

    def height(node):
        nonlocal max_dia
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        max_dia = max(max_dia, lh + rh + 1)
        return max(lh, rh) + 1

    height(root)
    return max_dia


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(diameter(root))
