class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        l, r = 0, n - 1

        while l + 1 < r:
            while l + 1 < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return True

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
            return True
        if nums[r] == target:
            return True
        return False
