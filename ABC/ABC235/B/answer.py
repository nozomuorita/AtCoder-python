n = int(input())
h = list(map(int, input().split()))

p = 0
ans = h[0]

while ((p != n-1) and (h[p] < h[p+1])):
    ans = h[p+1]
    p += 1

print(ans)