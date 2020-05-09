class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def serialize(root: TreeNode) -> str:
    """
    Given root, a TreeNode instance, that denotes the root of the binary tree.
    Return a string that serialize this binary tree.
    """
    if not root:
        return ""
    queue = [root]
    index = 0
    while index < len(queue):
        node = queue[index]
        if node:
            queue.append(node.left)
            queue.append(node.right)
        index += 1
    while queue[-1] is None:
        queue.pop()
    return ",".join(str(node.val) if node else "#" for node in queue)


def deserialize(string: str) -> TreeNode:
    """
    Given a string from the above serialization function,
    Return the root of the binary tree represented by string.
    """
    if len(string) == 0:
        return None
    string = string.split(",")
    root = TreeNode(int(string[0]))
    queue = [root]
    index = 0
    isLeft = True
    for s in string[1:]:
        cur = queue[index]
        if s != '#':
            node = TreeNode(int(s))
            queue.append(node)
            if isLeft:
                cur.left = node
            else:
                cur.right = node
        if not isLeft:
            index += 1
        isLeft = not isLeft
    return root


if __name__ == "__main__":
    string = "3,9,20,#,#,#,15"
    root = deserialize(string)
    decoded = serialize(root)
    print(decoded)
    assert string == decoded, "Wrong deserialization!"
