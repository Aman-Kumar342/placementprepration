def is_leaf(node):
    return node and node.left is None and node.right is None


class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def add_left(root, res):
    temp = root.left
    while temp:
        if not is_leaf(temp):
            res.append(temp.data)
        temp = temp.left if temp.left else temp.right


def add_right(root, res):
    temp = root.right
    tmp_res = []
    while temp:
        if not is_leaf(temp):
            tmp_res.append(temp.data)
        temp = temp.right if temp.right else temp.left
    res.extend(reversed(tmp_res))


def add_leaves(root, res):
    if root is None:
        return
    if is_leaf(root):
        res.append(root.data)
        return
    add_leaves(root.left, res)
    add_leaves(root.right, res)


def boundary(root):
    res = []
    if root is None:
        return res
    if not is_leaf(root):
        res.append(root.data)
    add_left(root, res)
    add_leaves(root, res)
    add_right(root, res)
    return res


def main():
    # Small demo tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(boundary(root))


if __name__ == "__main__":
    main()
