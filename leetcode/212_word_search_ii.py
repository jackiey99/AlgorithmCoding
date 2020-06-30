from typing import List

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]
        root.is_word = True
        root.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        m, n = len(board), len(board[0])
        result = set()
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, trie.root.children.get(
                    board[i][j]), set([(i, j)]), result)
        return list(result)

    def dfs(self, board, x, y, root, visit, result):
        if root is None:
            return
        if root.is_word:
            result.add(root.word)

        for dx, dy in DIRECTIONS:
            newx, newy = x + dx, y + dy
            if newx < 0 or newx >= len(board) or newy < 0 or newy >= len(board[0]):
                continue
            if (newx, newy) in visit:
                continue
            visit.add((newx, newy))
            self.dfs(board, newx, newy, root.children.get(
                board[newx][newy]), visit, result)
            visit.remove((newx, newy))


if __name__ == '__main__':
    s = Solution()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"],
             ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(s.findWords(board, words))
