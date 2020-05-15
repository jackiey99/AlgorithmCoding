from collections import defaultdict
from typing import List

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        longest = -1
        for i in range(m):
            for j in range(n):
                longest = max(longest, self.dfs(matrix, i, j, dp))
        return longest

    def dfs(self, matrix, x, y, dp):
        if (x, y) in dp:
            return dp[(x, y)]
        dp[(x, y)] = 1
        for dx, dy in DIRECTIONS:
            newx, newy = x + dx, y + dy
            if newx < 0 or newx >= len(matrix) or newy < 0 or newy >= len(matrix[0]):
                continue
            if matrix[x][y] < matrix[newx][newy]:
                dp[(x, y)] = max(dp[(x, y)], self.dfs(
                    matrix, newx, newy, dp) + 1)

        return dp[(x, y)]


if __name__ == "__main__":
    s = Solution()
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(s.longestIncreasingPath(matrix))
