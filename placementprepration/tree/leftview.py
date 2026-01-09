from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def left_view(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == 0:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res


if __name__ == "__main__":
    # simple demo
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(4)
    print(left_view(r))
