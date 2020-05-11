from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs(word, 0, "", res)
        return res

    def dfs(self, word, index, cur, res):
        if index == len(word):
            res.append(cur)
            return
        self.dfs(word, index + 1, cur + word[index], res)

        if not cur or not cur[-1].isdigit():
            for l in range(1, len(word) - index + 1):
                self.dfs(word, index + l, cur + str(l), res)


if __name__ == "__main__":
    s = Solution()
    input = "friends"
    print(s.generateAbbreviations(input))
