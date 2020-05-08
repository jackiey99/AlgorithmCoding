class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element

    @Time complexity: O(n)
    """

    def kthSmallest(self, k, nums):
        n = len(nums)
        if n == 0:
            return -1
        return self.quickSelect(nums, 0, n - 1, k - 1)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if right >= k and right >= start:
            return self.quickSelect(nums, start, right, k)
        if left <= k and left <= end:
            return self.quickSelect(nums, left, end, k)
        return nums[k]


if __name__ == "__main__":
    s = Solution()
    k = 3
    nums = [3, 4, 1, 2, 5]
    print(s.kthSmallest(k, nums))
