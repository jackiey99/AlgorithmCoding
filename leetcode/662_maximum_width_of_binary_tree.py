from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # queue of elements [(node, col_index)]
        if not root:
            return 0
        queue = deque()
        queue.append((root, 0))
        max_width = 0
        while queue:
            _, level_first_id = queue[0]
            for _ in range(len(queue)):
                node, node_id = queue.popleft()
                if node.left:
                    queue.append((node.left, node_id * 2))
                if node.right:
                    queue.append((node.right, node_id * 2 + 1))
            max_width = max(max_width, node_id - level_first_id + 1)
        return max_width
