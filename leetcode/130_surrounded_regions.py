from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        m, n = len(board), len(board[0])
        def rule(
            ij): return 0 <= ij[0] < m and 0 <= ij[1] < n and board[ij[0]][ij[1]] == 'O'
        queue = list(filter(rule, [coor for i in range(max(m, n))
                                   for coor in [(i, 0), (i, n - 1), (0, i), (m - 1, i)]]))
        while queue:
            i, j = queue.pop()
            board[i][j] = 'T'
            queue.extend(
                list(filter(rule, [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == '__main__':
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(board)
    print(board)
