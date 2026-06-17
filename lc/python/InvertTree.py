def invertTree(root):
    if not root:
        return
    invertTree(root.left)
    invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root