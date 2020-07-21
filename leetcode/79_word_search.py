from typing import List
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.search(board, i, j, 0, word, visit):
                    return True
        return False

    def search(self, board, i, j, index, word, visit):
        if index == len(word):
            return True
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or visit[i][j]:
            return False
        if board[i][j] != word[index]:
            return False

        visit[i][j] = True
        for dx, dy in DIRECTIONS:
            new_x, new_y = i + dx, j + dy
            if self.search(board, new_x, new_y, index + 1, word, visit):
                return True
        visit[i][j] = False
        return False


if __name__ == '__main__':
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print(s.exist(board, word))
