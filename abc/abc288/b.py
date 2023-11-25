n, k = map(int, input().split())
s = sorted([input() for _ in range(n)][:k])
for i in s: print(i)