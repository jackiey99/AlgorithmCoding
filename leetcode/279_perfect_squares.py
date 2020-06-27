import sys
import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize for _ in range(n + 1)]
        for i in range(int(math.sqrt(n)) + 1):
            dp[i * i] = 1
        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i - j * j] + 1, dp[i])

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(20))
