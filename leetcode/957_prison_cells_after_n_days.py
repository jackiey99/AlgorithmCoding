from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        flag = False
        seen = {}
        while N > 0:
            if not flag:
                curr = str(cells)
                if curr in seen:
                    N %= seen[str(cells)] - N
                    flag = True
                else:
                    seen[str(cells)] = N
            if N > 0:
                cells = self.nextDay(cells)
                N -= 1
        return cells

    def nextDay(self, cells):
        cells = [0] + [cells[i - 1] ^ cells[i + 1]
                       ^ 1 for i in range(1, 7)] + [0]
        return cells


if __name__ == '__main__':
    s = Solution()
    cells = [1, 1, 0, 1, 1, 0, 1, 1]
    N = 6
    print(s.prisonAfterNDays(cells, N))
