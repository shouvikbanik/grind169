def invert_binary_tree(root):
    if not root:
        return root
    temp = root.left
    root.left = root.right
    root.right = temp
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root
