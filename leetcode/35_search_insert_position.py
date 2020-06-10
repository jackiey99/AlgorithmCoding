from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        if nums[right] < target:
            return right + 1
        if nums[left] < target:
            return right
        return left


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 5, 7]
    target = 8
    print(s.searchInsert(nums, target))
