from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for n in nums:
            ones = (~twos) & (ones ^ n)
            twos = (~ones) & (twos ^ n)
        return ones


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1, 1, 3, 3, 3]
    print(s.singleNumber(nums))
