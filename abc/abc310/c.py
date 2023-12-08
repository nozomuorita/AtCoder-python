n = int(input())
s = [input() for _ in range(n)]

words = set()
ans = 0
for i in range(n):
    if (s[i] not in words) and (s[i][::-1] not in words):
        ans += 1
        words.add(s[i])
        words.add(s[i][::-1])

print(ans)
