from collections import deque, defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def vertical_order(root):
    if not root:
        return []
    col_map = defaultdict(list)
    q = deque([(root, 0)])
    while q:
        node, col = q.popleft()
        col_map[col].append(node.val)
        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))
    return [col_map[c] for c in sorted(col_map.keys())]


if __name__ == "__main__":
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)
    print(vertical_order(r))
