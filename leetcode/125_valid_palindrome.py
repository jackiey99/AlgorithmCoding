class Solution:
    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            while low < high and not s[high].isalnum():
                high -= 1
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    string = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(string))
