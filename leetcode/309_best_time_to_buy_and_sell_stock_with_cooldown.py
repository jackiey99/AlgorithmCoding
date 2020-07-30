from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, hold, reset = float('-inf'), float('-inf'), 0

        for p in prices:
            prev_sold = sold
            sold = hold + p
            hold = max(hold, reset - p)
            reset = max(reset, prev_sold)
        return max(sold, reset)


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 0, 2]
    print(s.maxProfit(prices))
