def lowest_common_ancestor(root, p, q):
    if p.val > q.val:
        temp = p
        p = q
        q = temp
    if p.val < root.val < q.val:
        return root
    elif root.val == p.val or root.val == q.val:
        return root
    elif root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    else:
        return lowest_common_ancestor(root.right, p, q)
