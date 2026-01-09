from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_view(root):
    if not root:
        return []
    mpp = {}
    q = deque([(root, 0)])
    while q:
        node, line = q.popleft()
        mpp[line] = node.val
        if node.left:
            q.append((node.left, line - 1))
        if node.right:
            q.append((node.right, line + 1))
    return [mpp[key] for key in sorted(mpp.keys())]


def main():
    # Example tree 20 / 8\22
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    print(" ".join(map(str, bottom_view(root))))


if __name__ == "__main__":
    main()
