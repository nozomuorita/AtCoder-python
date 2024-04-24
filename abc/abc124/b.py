n = int(input())
a = list(map(int, input().split()))

mx = a[0]
ans = 1
for i in a[1:]:
  if i>=mx: ans+=1
  mx = max(mx, i)

print(ans)