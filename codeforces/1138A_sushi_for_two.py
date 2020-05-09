from itertools import groupby
n = input()
consecutive_len = [len([*g]) for k, g in groupby(input().split())]
ans = 2 * max(map(min, zip(consecutive_len, consecutive_len[1:])))
print(ans)
