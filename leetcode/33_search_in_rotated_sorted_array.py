class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l + 1 < r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[r]:  # right side is sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
