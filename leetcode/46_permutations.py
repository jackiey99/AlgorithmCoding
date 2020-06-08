from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        visit = [False for _ in range(n)]
        self.dfs(nums, [], results, visit)
        return results

    def dfs(self, nums, path, results, visit):
        if len(path) == len(nums):
            results.append(list(path))
            return
        for i in range(len(nums)):
            if visit[i]:
                continue
            visit[i] = True
            path.append(nums[i])
            self.dfs(nums, path, results, visit)
            path.pop()
            visit[i] = False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    s = Solution()
    print(s.permute(nums))
