import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        fact = math.factorial(n)
        res = []
        k -= 1
        for i in range(n, 0, -1):
            fact = fact // i
            q, k = divmod(k, fact)
            res.append(digits[q])
            digits.remove(digits[q])
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(5, 9))
