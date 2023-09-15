n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]

h.sort()
ans = 10**9
for i in range(n):
    if (i+k-1)>=n:
        break
    dist = h[i+k-1] - h[i]
    if dist < ans:
        ans = dist
print(ans)