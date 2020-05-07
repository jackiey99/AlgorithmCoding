n = int(input())
strings = sorted((input() for _ in range(n)), key=lambda x: len(x))
if all(strings[i] in strings[i + 1] for i in range(n - 1)):
    print("YES")
    for s in strings:
        print(s)
else:
    print("NO")
