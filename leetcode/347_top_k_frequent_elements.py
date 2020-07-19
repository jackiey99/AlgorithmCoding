from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = []
        for n in nums:
            freq[n] += 1
        for n in freq:
            heappush(heap, (-freq[n], n))
        res = []
        for _ in range(k):
            _, val = heappop(heap)
            res.append(val)
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    s = Solution()
    print(s.topKFrequent(nums, 2))
