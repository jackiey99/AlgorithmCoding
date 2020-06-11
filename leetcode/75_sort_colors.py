from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            else:
                i += 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 0, 0, 2, 0, 1]
    s.sortColors(nums)
    print(nums)
