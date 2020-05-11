# Definition for a binary tree node.
from serialize_and_deserialize_binary_tree import deserialize


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.left, self.right = 0, 0
        self.dfs(root, x)
        if max(self.left, self.right, n - 1 - self.left - self.right) > n // 2:
            return True
        return False

    def dfs(self, root, x):
        if root is None:
            return 0
        l = self.dfs(root.left, x)
        r = self.dfs(root.right, x)
        if root.val == x:
            self.left = l
            self.right = r
        return 1 + l + r


if __name__ == "__main__":
    s = Solution()
    root = deserialize("1,2,3,4,5,6,7,8,9,10,11")
    print(s.btreeGameWinningMove(root, 11, 3))
