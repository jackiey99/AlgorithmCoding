from typing import List

"""
some useful xor properties:
A xor A = 0
A xor 0 = A
"""


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        res = []
        prefix = {}
        prefix[-1] = 0
        for i in range(n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        for s, e in queries:
            res.append(prefix[e] ^ prefix[s - 1])
        return res


if __name__ == "__main__":
    s = Solution()
    arr = [4, 8, 2, 10]
    queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
    print(s.xorQueries(arr, queries))
