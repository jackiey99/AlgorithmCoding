from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        self.dfs(graph, 0, [0], target, res)
        return res

    def dfs(self, graph, cur, path, target, res):
        if cur == target:
            res.append(list(path))
            return
        for nbr in graph[cur]:
            path.append(nbr)
            self.dfs(graph, nbr, path, target, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    graph = [[1, 2], [3], [3], []]
    print(s.allPathsSourceTarget(graph))
