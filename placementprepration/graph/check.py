from collections import deque
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_view(root):
    if not root:
        return []
    hd_map = {}
    q = deque([(root, 0)])
    while q:
        node, hd = q.popleft()
        hd_map[hd] = node.val
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    return [hd_map[x] for x in sorted(hd_map.keys())]


def main():
    # Placeholder tree: build simple binary tree 1,2,3 for demonstration
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(" ".join(map(str, bottom_view(root))))


if __name__ == "__main__":
    main()
