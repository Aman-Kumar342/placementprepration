from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level_vals = []
        for _ in range(len(q)):
            node = q.popleft()
            level_vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level_vals)
    return res


if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    print(level_order(r))
