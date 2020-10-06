class Solution:
    memo1 = {}
    memo2 = {}
    def minimumOneBitOperations(self, n: int) -> int:
        s = bin(n)[2:]
        return self.dfs(s)
    
    def dfs(self, s):
        if s == '0': return 0
        if s == '1': return 1
        if s in self.memo1: return self.memo1[s]
        if s[0]=='0': return self.dfs(s[1:])

        m = s[1:]
        p = ''.join(['1'] + ['0' for _ in range(len(m)-1)])
        self.memo1[s] = self.dfs2(m) + 1 + self.dfs(p)
        return self.memo1[s]
    
    def dfs2(self, s):
        if s == '0': return 1
        if s == '1': return 0
        if s in self.memo2: return self.memo2[s]
        
        if s[0] == '1':
            self.memo2[s] = self.dfs(s[1:])
        else:
            m = s[1:]
            p = ''.join(['1'] + ['0' for _ in range(len(m)-1)])
            self.memo2[s] = self.dfs2(m) + 1 + self.dfs(p)
        
        return self.memo2[s]

if __name__ == "__main__":
    s = Solution()
    n = 333
    print(s.minimumOneBitOperations(n))
