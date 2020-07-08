from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [[0 for _ in range(2001)] for _ in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1

        for i in range(1, len(nums)):
            for j in range(-1000, 1001):
                if j + nums[i] + 1000 < 2001:
                    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000]
                    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000]

        return dp[len(nums) - 1][S + 1000] if S <= 1000 else 0


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    print(s.findTargetSumWays(nums, S))
