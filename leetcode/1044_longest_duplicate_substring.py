from functools import reduce


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            pos = self.test(mid, S)
            if pos:
                lo = mid
                res = pos
            else:
                hi = mid - 1
        return S[res:res + lo]

    def test(self, L, S):
        A = [ord(s) - ord('a') for s in S]
        mod = 2**63 - 1
        p = pow(26, L, mod)
        cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
        seen = {cur}
        for i in range(L, len(S)):
            cur = (cur * 26 + A[i] - A[i - L] * p) % mod
            if cur in seen:
                return i - L + 1
            seen.add(cur)


if __name__ == '__main__':
    s = Solution()
    S = "banana"
    print(s.longestDupSubstring(S))
