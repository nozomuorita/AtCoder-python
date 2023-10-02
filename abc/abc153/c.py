n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort(reverse=True)

if k>=n:
    ans = 0
else:
    ans = sum(h[k:])
print(ans)