n, m = map(int, input().split())
left, right = 0, 10**5+10
for i in range(m):
    l, r = map(int, input().split())
    left = max(l, left)
    right = min(r, right)
print(max(right-left+1, 0))