from collections import Counter


class Solution:
    def numWays(self, s: str) -> int:
        cnt = Counter(s)
        if cnt['1'] % 3 != 0:
            return 0
        if cnt['1'] == 0:
            ans = (cnt['0'] - 1) * (cnt['0'] - 2) // 2
            return ans % (10**9 + 7)
        pos = [0] * cnt['1']
        inc = 0
        for i, char in enumerate(s):
            if char == '1':
                pos[inc] = i
                inc += 1
        t = cnt['1'] // 3
        ans = (pos[t] - pos[t - 1]) * (pos[2 * t] - pos[2 * t - 1])
        return ans % (10**9 + 7)


if __name__ == "__main__":
    s = Solution()
    string = "100100010100110"
    print(s.numWays(string))
