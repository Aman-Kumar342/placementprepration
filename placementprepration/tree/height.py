from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def height_iterative(root):
    if not root:
        return 0
    q = deque([root])
    h = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        h += 1
    return h


if __name__ == "__main__":
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    print(height(r), height_iterative(r))
