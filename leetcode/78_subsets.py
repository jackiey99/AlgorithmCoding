from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, 0, [], ans)
        return ans

    def dfs(self, nums, start, items, ans):
        ans.append(list(items))

        for i in range(start, len(nums)):
            items.append(nums[i])
            self.dfs(nums, i + 1, items, ans)
            items.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))
