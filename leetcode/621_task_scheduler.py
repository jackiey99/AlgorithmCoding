from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.defaultdict(int)
        max_cnt = 0
        for t in tasks:
            cnt[t] += 1
            max_cnt = max(max_cnt, cnt[t])

        result = (max_cnt - 1) * (n + 1)
        for v in cnt.values():
            if v == max_cnt:
                result += 1

        result = max(result, len(tasks))

        return result


if __name__ == '__main__':
    s = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(s.leastInterval(tasks, n))
