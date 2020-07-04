class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            res.append(min(res[p2] * 2, res[p3] * 3, res[p5] * 5))
            if res[-1] == res[p2] * 2:
                p2 += 1
            if res[-1] == res[p3] * 3:
                p3 += 1
            if res[-1] == res[p5] * 5:
                p5 += 1
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))
