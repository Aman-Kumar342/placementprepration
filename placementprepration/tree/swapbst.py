import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root, vals):
    if not root:
        return
    inorder(root.left, vals)
    vals.append(root.val)
    inorder(root.right, vals)


def replace_with_sorted(root, vals_iter):
    if not root:
        return
    replace_with_sorted(root.left, vals_iter)
    root.val = next(vals_iter)
    replace_with_sorted(root.right, vals_iter)


def recover_bst(root):
    vals = []
    inorder(root, vals)
    vals.sort()
    replace_with_sorted(root, iter(vals))


def main():
    # Placeholder for building a tree and calling recover_bst
    pass


if __name__ == "__main__":
    main()
