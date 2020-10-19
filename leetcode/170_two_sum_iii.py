class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.count:
            complement = value - num
            if num != complement:
                if complement in self.count:
                    return True
            else:
                if self.count[num] > 1:
                    return True

        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
