from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        dp = [1] * n
        prev = [-1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == dp[j] + 1:
                        prev[i] = j

        maxlen = -1
        idx = -1
        for i in range(n):
            if dp[i] > maxlen:
                maxlen = dp[i]
                idx = i
        res = []
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 4, 8]
    print(s.largestDivisibleSubset(nums))
