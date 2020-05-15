from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        lst_values = self.dic[key]
        left, right = 0, len(lst_values) - 1
        if lst_values[left][1] > timestamp:
            return ""
        if lst_values[right][1] <= timestamp:
            return lst_values[right][0]
        while left + 1 < right:
            mid = (left + right) // 2
            if lst_values[mid][1] == timestamp:
                return lst_values[mid][0]
            if lst_values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if lst_values[right][1] <= timestamp:
            return lst_values[right][0]
        return lst_values[left][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
