class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            if total < n:
                start = mid + 1
            else:
                end = mid - 1
        return end


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(10))
