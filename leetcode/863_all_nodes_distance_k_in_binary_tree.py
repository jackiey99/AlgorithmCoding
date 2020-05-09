from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root is None:
            return []
        parents = {}
        self.getParents(root, parents)
        visit = set()
        queue = deque()
        queue.append((target, 0))
        res = []
        while queue:
            node, level = queue.popleft()
            if level == K:
                res.append(node.val)
            visit.add(node)
            if node.left and node.left not in visit:
                queue.append((node.left, level + 1))
            if node.right and node.right not in visit:
                queue.append((node.right, level + 1))
            if node in parents and parents[node] not in visit:
                queue.append((parents[node], level + 1))
        return res

    def getParents(self, node, parents):
        if node is None:
            return
        if node.left:
            parents[node.left] = node
            self.getParents(node.left, parents)
        if node.right:
            parents[node.right] = node
            self.getParents(node.right, parents)
