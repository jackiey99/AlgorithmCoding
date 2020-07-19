from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = {i: [] for i in range(numCourses)}
        degs = [0] * numCourses

        for i, j in prerequisites:
            edges[j].append(i)
            degs[i] += 1

        q = deque()

        for i in range(numCourses):
            if degs[i] == 0:
                q.append(i)
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nbr in edges[cur]:
                degs[nbr] -= 1
                if degs[nbr] == 0:
                    q.append(nbr)
        if len(res) == numCourses:
            return res
        else:
            return []


if __name__ == '__main__':
    s = Solution()
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    numCourses = 4
    print(s.findOrder(numCourses, prerequisites))
