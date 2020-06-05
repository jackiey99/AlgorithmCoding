class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        random_number = self.total_sum * random.random()
        low, high = 0, len(self.prefix) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if random_number > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        if self.prefix[low] > random_number:
            return low
        return high


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
