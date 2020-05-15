class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal, res = 0, 0
        for char in s:
            if char == 'L':
                bal += 1
            if char == 'R':
                bal -= 1
            if bal == 0:
                res += 1
        return res

    def printBalancedStrings(self, s: str):
        bal = 0
        res = []
        start = 0
        for i, char in enumerate(s):
            if char == 'L':
                bal += 1
            if char == 'R':
                bal -= 1
            if bal == 0:
                res.append(s[start:i + 1])
                start = i + 1
        return res


if __name__ == "__main__":
    s = Solution()
    string = "RLRRRLLRLL"
    print(s.balancedStringSplit(string))
    print(s.printBalancedStrings(string))
