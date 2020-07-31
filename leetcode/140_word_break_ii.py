from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []
        for word in wordDict:
            prefix = s[:len(word)]
            if prefix != word:
                continue
            if len(word) == len(s):
                partitions.append(word)
            else:
                res = self.dfs(s[len(word):], wordDict, memo)

                for r in res:
                    partitions.append(prefix + ' ' + r)

        memo[s] = partitions
        return partitions


if __name__ == '__main__':
    s = Solution()
    string = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(s.wordBreak(string, wordDict))
