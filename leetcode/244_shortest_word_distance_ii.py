from collections import defaultdict
class WordDistance:

    def __init__(self, words: List[str]):
        self.loc = defaultdict(list)
        for i, w in enumerate(words):
            self.loc[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        locs1, locs2 = self.loc[word1], self.loc[word2]
        p1, p2 = 0, 0
        res = float('inf')
        while p1 < len(locs1) and p2 < len(locs2):
            res = min(res, abs(locs1[p1] - locs2[p2]))
            if locs1[p1] < locs2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
