# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for _ in range(10):
            ind = random.randint(0, len(wordlist) - 1)
            s = wordlist[ind]

            k = master.guess(s)
            if k == len(s):
                return
            candidates = []
            for word in wordlist:
                if s == word:
                    continue
                if self.similarity(s, word) == k:
                    candidates.append(word)
            wordlist = candidates

    def similarity(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                count += 1

        return count
