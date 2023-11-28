n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    if a[i]<l:
        ans.append(l)
    elif a[i]>r:
        ans.append(r)
    else:
        ans.append(a[i])
print(*ans)