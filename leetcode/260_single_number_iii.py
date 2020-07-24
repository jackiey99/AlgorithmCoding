from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        right_most = xor & (-xor)
        x = 0
        for num in nums:
            if num & right_most:
                x ^= num
        y = xor ^ x
        return [x, y]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 2, 5, 1]
    print(s.singleNumber(nums))
