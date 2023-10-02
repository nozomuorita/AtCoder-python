n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
for i in range(n):
    if a[i] < sum(a)/(4*m):
        continue
    if ans >= m:
        break
    ans += 1
    
if ans >= m:
    print('Yes')
else:
    print('No')