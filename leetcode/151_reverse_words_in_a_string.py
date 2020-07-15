class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        i = len(s) - 1

        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            if i < 0:
                break

            if len(res) > 0:
                res += ' '

            check_pt = i + 1
            while i >= 0 and s[i] != ' ':
                i -= 1
            for tmp in range(i + 1, check_pt):
                res += s[tmp]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("  hello   world!  "))
