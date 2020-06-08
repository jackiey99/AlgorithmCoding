from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        visit = [False for _ in range(len(nums))]
        self.dfs(nums, [], results, visit)
        return results

    def dfs(self, nums, path, results, visit):
        if len(path) == len(nums):
            results.append(list(path))
            return
        for i in range(len(nums)):
            if visit[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visit[i - 1]:
                continue
            visit[i] = True
            path.append(nums[i])
            self.dfs(nums, path, results, visit)
            path.pop()
            visit[i] = False


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = Solution()
    print(s.permuteUnique(nums))
