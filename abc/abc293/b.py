n = int(input())
a = list(map(int, input().split()))

call = [-1]*n
for i in range(n):
    if call[i]==-1: call[a[i]-1]=1

ans = []
for i in range(n):
    if call[i]==-1: ans.append(i+1)

print(len(ans))
print(*ans)