from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_pat = defaultdict(int)
        for char in t:
            t_pat[char] += 1

        l, r = 0, 0
        min_len = len(s) + 1
        res_l, res_r = 0, 0
        s_pat = defaultdict(int)
        for r in range(len(s)):
            s_pat[s[r]] += 1
            while self.check(s_pat, t_pat):
                min_len = min(min_len, r-l+1)
                if min_len == r-l+1:
                    res_l, res_r = l, r
                s_pat[s[l]] -= 1
                l += 1
        if min_len < len(s) + 1:
            return s[res_l:res_r+1]
        return ""

    def check(self, s_pat, t_pat):
        # check whether s_pat can cover t_pat
        for k in t_pat:
            if k not in s_pat:
                return False
            if s_pat[k] < t_pat[k]:
                return False
        return True
