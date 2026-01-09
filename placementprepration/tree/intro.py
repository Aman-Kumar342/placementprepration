from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


def build_tree_from_list(values):
    # Build tree from preorder list with -1 indicating null
    def helper(it):
        try:
            val = next(it)
        except StopIteration:
            return None
        if val == -1:
            return None
        node = Node(val)
        node.left = helper(it)
        node.right = helper(it)
        return node
    return helper(iter(values))


if __name__ == "__main__":
    vals = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    root = build_tree_from_list(vals)
    print("Preorder", preorder(root))
    print("Inorder", inorder(root))
    print("Postorder", postorder(root))
    print("Level order", level_order(root))
