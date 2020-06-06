from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []

        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in sorted_people:
            res.insert(p[1], p)
        return res


if __name__ == "__main__":
    s = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(s.reconstructQueue(people))
