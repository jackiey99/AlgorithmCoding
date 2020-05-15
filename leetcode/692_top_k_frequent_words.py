from heapq import heappush, heappop
from collections import defaultdict
from typing import List


class WrapString:
    def __init__(self, string):
        self.val = string

    def __lt__(self, other):
        return self.val > other.val


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for w in words:
            freq[w] += 1
        heap = []
        for w, v in freq.items():
            heappush(heap, (v, WrapString(w)))
            if len(heap) > k:
                heappop(heap)
        res = []
        while heap:
            _, w = heappop(heap)
            res.append(w.val)
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    print(s.topKFrequent(words, 3))
