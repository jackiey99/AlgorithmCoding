class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.subsets(nums, 0, [], res)
        return res
        
    def subsets(self, nums, index, cur, res):
        if len(nums) >= index and len(cur) >= 2:
            res.append(cur[:])
        used = {}
        for i in range(index, len(nums)):
            if len(cur) > 0 and cur[-1] > nums[i]: continue
            if nums[i] in used: continue
            used[nums[i]] = True
            cur.append(nums[i])
            self.subsets(nums, i+1, cur, res)
            cur.pop()
