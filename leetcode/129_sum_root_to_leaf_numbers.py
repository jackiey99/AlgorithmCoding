# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, root, path):
        if root is None:
            return
        # at leaf
        if root.left is None and root.right is None:
            path = path * 10 + root.val
            self.sum += path
            return
        path = path * 10 + root.val
        self.dfs(root.left, path)
        self.dfs(root.right, path)
