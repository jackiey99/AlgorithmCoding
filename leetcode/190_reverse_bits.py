class Solution:
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n > 0:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(12))
