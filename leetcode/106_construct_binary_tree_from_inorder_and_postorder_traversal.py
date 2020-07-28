# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        val2ind = {v: i for i, v in enumerate(inorder)}

        def helper(low, high):
            if low > high:
                return None
            root = TreeNode(postorder.pop())
            mid = val2ind[root.val]
            root.right = helper(mid + 1, high)
            root.left = helper(low, mid - 1)
            return root
        return helper(0, len(inorder) - 1)
