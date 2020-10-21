class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        M = 10**9 + 7
        N = len(S)
        next = [[N for _ in range(N)] for _ in range(4)]
        prev = [[-1 for _ in range(N)] for _ in range(4)]
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for k in range(4):
            i = 0
            for j in range(N):
                if S[j] != chr(ord('a') + k):
                    continue
                while i <= j:
                    next[k][i] = j
                    i += 1

        for k in range(4):
            i = N - 1
            for j in range(N - 1, -1, -1):
                if S[j] != chr(ord('a') + k):
                    continue
                while i >= j:
                    prev[k][i] = j
                    i -= 1

        for i in range(N):
            dp[i][i] = 1

        for l in range(2, N + 1):
            for i in range(0, N - l + 1):
                j = i + l - 1
                for k in range(4):
                    p, q = next[k][i], prev[k][j]
                    if p < q:
                        dp[i][j] += dp[p + 1][q - 1] + 1
                    if p <= j:
                        dp[i][j] += 1
                    dp[i][j] %= M

        return dp[0][N - 1]
