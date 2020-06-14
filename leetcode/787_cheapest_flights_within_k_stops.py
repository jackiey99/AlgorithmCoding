from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        w = defaultdict(dict)
        for a, b, p in flights:
            w[a][b] = p
        heap = [(0, src, K + 1)]
        while heap:
            p, node, k = heappop(heap)
            if node == dst:
                return p
            if k > 0:
                for nbr in w[node]:
                    heappush(heap, (p + w[node][nbr], nbr, k - 1))
        return -1


if __name__ == '__main__':
    s = Solution()
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    print(s.findCheapestPrice(n, edges, src, dst, k))
