from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twosum(nums, i + 1, -nums[i], res)
        return res

    def twosum(self, numbers, left, target, res):
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                res.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
