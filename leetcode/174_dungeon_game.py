import sys
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = (need, 1)[need <= 0]
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(s.calculateMinimumHP(dungeon))
