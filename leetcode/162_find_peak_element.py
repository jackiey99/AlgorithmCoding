class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] < nums[mid + 1]:
                lo = mid
            else:
                hi = mid
        return lo if nums[lo] > nums[hi] else hi
