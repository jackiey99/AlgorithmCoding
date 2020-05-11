# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.isUniTree(root)
        return self.count

    def isUniTree(self, root):
        if root is None:
            return True
        is_uni_left = self.isUniTree(root.left)
        is_uni_right = self.isUniTree(root.right)
        if (is_uni_left and is_uni_right and
            (root.left is None or root.val == root.left.val) and
                (root.right is None or root.val == root.right.val)):
            self.count += 1
            return True
        return False

        """
        Bug:
        Initially, I did like following, but since python uses lazy evaluation for
        if conditions, the self.isUniTree(root.right) may not be executed if self.isUniTree(root.left) is False,
        hence the dfs on the right children may not be done. So we need to separate the two conditions.
        """
        # if self.isUniTree(root.left)
        # and self.isUniTree(root.right) \
        #    and (root.left is None or root.val == root.left.val) \
        #    and (root.right is None or root.val == root.right.val):
        #     self.count += 1
        #     return True
        # return False
