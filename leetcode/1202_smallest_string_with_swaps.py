from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    """
    Key points: realize that this can be solved using graphs
                use union-find to get the connected-components in the graph
    """
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        father_x = self.find(x)
        father_y = self.find(y)
        if father_x != father_y:
            self.father[father_x] = father_y

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        self.father = [i for i in range(n)]
        for x, y in pairs:
            self.union(x, y)
        connected_components = defaultdict(list)
        for i in range(n):
            heappush(connected_components[self.find(i)], s[i])
        res = ""
        for i in range(n):
            res += heappop(connected_components[self.find(i)])
        return res


if __name__ == '__main__':
    s = Solution()
    string = "cba"
    pairs = [[0, 1], [1, 2]]
    print(s.smallestStringWithSwaps(string, pairs))
