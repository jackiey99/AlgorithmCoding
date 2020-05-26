class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0 for _ in range(10)] for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[7][9] = skip[9][7] = 8
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        vis = [False for _ in range(10)]
        res = 0
        for i in range(m, n + 1):
            res += self.dfs(1, i - 1, vis, skip) * 4
            res += self.dfs(2, i - 1, vis, skip) * 4
            res += self.dfs(5, i - 1, vis, skip)
        return res

    def dfs(self, cur, remaining, vis, skip):
        if remaining < 0:
            return 0
        if remaining == 0:
            return 1
        vis[cur] = True
        res = 0
        for i in range(1, 10):
            if not vis[i] and (skip[cur][i] == 0 or vis[skip[cur][i]]):
                res += self.dfs(i, remaining - 1, vis, skip)
        vis[cur] = False
        return res


if __name__ == "__main__":
    s = Solution()
    m, n = 2, 3
    print(s.numberOfPatterns(m, n))
