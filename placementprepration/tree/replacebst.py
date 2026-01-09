import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_collect(root, vals):
    if not root:
        return
    inorder_collect(root.left, vals)
    vals.append(root.val)
    inorder_collect(root.right, vals)


def inorder_assign(root, vals_iter):
    if not root:
        return
    inorder_assign(root.left, vals_iter)
    root.val = next(vals_iter)
    inorder_assign(root.right, vals_iter)


def recover_bst(root):
    vals = []
    inorder_collect(root, vals)
    vals.sort()
    inorder_assign(root, iter(vals))


def main():
    # Placeholder: build tree externally, then call recover_bst(root)
    pass


if __name__ == "__main__":
    main()
