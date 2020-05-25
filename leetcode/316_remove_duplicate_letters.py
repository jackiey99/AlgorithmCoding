class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurence = {c: i for i, c in enumerate(s)}
        seen = set()
        stack = []
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurence[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()
    string = "cbacdcbc"
    print(s.removeDuplicateLetters(string))
