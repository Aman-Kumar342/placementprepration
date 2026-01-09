from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def top_view(root):
    if not root:
        return []
    hd_map = {}
    q = deque([(root, 0)])
    while q:
        node, hd = q.popleft()
        if hd not in hd_map:
            hd_map[hd] = node.val
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    return [hd_map[k] for k in sorted(hd_map.keys())]


if __name__ == "__main__":
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.right = Node(4)
    r.left.right.right = Node(5)
    r.left.right.right.right = Node(6)
    print(top_view(r))
