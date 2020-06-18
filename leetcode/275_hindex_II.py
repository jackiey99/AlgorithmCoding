from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] == n - mid:
                return n - mid
            if citations[mid] < n - mid:
                low = mid + 1
            else:
                high = mid - 1
        return n - low


if __name__ == '__main__':
    s = Solution()
    citations = [0, 1, 3, 5, 6]
    print(s.hIndex(citations))
