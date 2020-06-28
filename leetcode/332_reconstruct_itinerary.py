from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for a, b in tickets:
            heappush(edges[a], b)
        res = []

        def dfs(origin, res):
            if len(res) == len(tickets) + 1:
                return
            while edges[origin]:
                next_dest = heappop(edges[origin])
                dfs(next_dest, res)
            res.append(origin)
        dfs("JFK", res)
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
        "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(s.findItinerary(tickets))
