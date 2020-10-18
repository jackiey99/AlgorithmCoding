class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            count += 1
            if random.randint(0, count-1) == 0:
                res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
