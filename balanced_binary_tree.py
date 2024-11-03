def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.left))


def balanced_binary_tree(root):
    if not root or (root.left is None and root.right is None):
        return True
    else:
        if abs(height(root.left) - height(root.right)) >= 2:
            return False
        else:
            return balanced_binary_tree(root.left) and balanced_binary_tree(root.right)
