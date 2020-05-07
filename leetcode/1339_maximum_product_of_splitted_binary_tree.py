# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        all_tree_sums = []
        total_sum = self.dfs(root, all_tree_sums)
        max_product = 0
        for s1 in all_tree_sums:
            s2 = total_sum - s1
            max_product = max(max_product, s1 * s2)
        return max_product % 1000000007

    def dfs(self, root, all_tree_sums):
        if root is None:
            return 0
        left_sum = self.dfs(root.left, all_tree_sums)
        right_sum = self.dfs(root.right, all_tree_sums)
        total_sum = left_sum + root.val + right_sum
        all_tree_sums.append(total_sum)
        return total_sum
