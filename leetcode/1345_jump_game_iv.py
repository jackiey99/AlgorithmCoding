from collections import defaultdict, deque
from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: 
            return 0
        
        pos = defaultdict(list)
        for i, a in enumerate(arr):
            pos[a].append(i)
        
        queue = deque()
        queue.append(0)
        visited = {0}
        step = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n-1:
                    return step
                
                if cur + 1 < n and cur + 1 not in visited:
                    visited.add(cur+1)
                    queue.append(cur+1)
                
                if cur - 1 >=0 and cur -1 not in visited:
                    visited.add(cur -1)
                    queue.append(cur-1)
                    
                for p in pos[arr[cur]]:
                    if p not in visited:
                        visited.add(p)
                        queue.append(p)
                
                del pos[arr[cur]]
                
            step += 1
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
