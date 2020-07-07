DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += self.sum_adj(grid, i, j)
        return ans

    def sum_adj(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or grid[new_x][new_y] == 0:
                perimeter += 1

        return perimeter


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 1], [1, 1]]
    print(s.islandPerimeter(grid))
