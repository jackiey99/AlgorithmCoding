from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] *= -1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
