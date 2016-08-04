def is_tree_same(t1, t2):
    if t1 is None and t2 is None:
        return True

    if t1 and t2 and t1.val == t2.val:
        return is_tree_same(t1.left, t2.left) and is_tree_same(t1.right, t2.right)

    return False


def is_tree_same_dfs(t1, t2):
    if t1 is None and t2 is None:
        return True

    stack = [(t1, t2)]
    while stack:
        n1, n2 = stack.pop()
        if n1 == None or n2 == None:
            continue
        elif n1 and n2 and n1.val == n2.val:
            stack.append(n1.left, n2.left)
            stack.append(n1.righ, n2.right)
        else:
            return False
    return True


def invert_binary_tree(root):
    if root is None:
        return None

    if root.left:
        invert_binary_tree(root.left)
    if root.right:
        invert_binary_tree(root.right)
    root.left, root.right = root.right, root.left
    return root


def invertTree_dfs(root):
    if root is None:
        return None
    queue = [root]
    while queue:
        front = queue.pop(0)
        if front.left:
            queue.append(front.left)
        if front.right:
            queue.append(front.right)
        front.left, front.right = front.right, front.left
    return root
