from collections import defaultdict, deque
import sys
from typing import List

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        dist = [[0 for _ in range(n)] for _ in range(m)]
        visit = defaultdict(int)
        num_building = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, visit, dist, num_building)
                    num_building += 1

        min_dist = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and visit[(i, j)] == num_building:
                    min_dist = min(min_dist, dist[i][j])

        if min_dist != sys.maxsize:
            return min_dist
        return -1

    def bfs(self, grid, x, y, visit, dist, num_building):
        queue = deque()
        queue.append((x, y))
        m, n = len(grid), len(grid[0])
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= m or newy < 0 or newy >= n:
                        continue
                    if grid[newx][newy] == 2 or grid[newx][newy] == 1:
                        continue
                    if visit[(newx, newy)] == num_building:
                        queue.append((newx, newy))
                        dist[newx][newy] += step
                        visit[(newx, newy)] += 1


if __name__ == "__main__":
    grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    s = Solution()
    print(s.shortestDistance(grid))
