from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = high - 1
        return nums[low]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 2, 0, 1]
    print(s.findMin(nums))
