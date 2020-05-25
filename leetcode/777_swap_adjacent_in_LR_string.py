class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        pos_start = [(i, c)
                     for i, c in enumerate(start) if c == 'L' or c == 'R']
        pos_end = [(i, c) for i, c in enumerate(end) if c == 'L' or c == 'R']

        if len(pos_start) != len(pos_end):
            return False

        for (i, c1), (j, c2) in zip(pos_start, pos_end):
            if c1 != c2:
                return False
            if c1 == 'L':
                if i < j:
                    return False
            if c1 == 'R':
                if i > j:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    print(s.canTransform(start, end))
