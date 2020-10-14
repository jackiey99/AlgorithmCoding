# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return  "#"

        return (str(root.val) + ","
                + self.serialize(root.left) + ","
                + self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(","))
        return self.buildTree(data)

    def buildTree(self, data):
        cur = data.popleft()
        if cur == "#": return None
        root = TreeNode(int(cur))
        root.left = self.buildTree(data)
        root.right = self.buildTree(data)
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
