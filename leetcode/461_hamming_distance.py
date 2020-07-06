class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0

        while xor:
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance


if __name__ == '__main__':
    s = Solution()
    x = 9
    y = 23
    print(s.hammingDistance(x, y))
