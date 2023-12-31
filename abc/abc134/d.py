n = int(input())
a = list(map(int, input().split()))

boll = [0]*(n+1)
for i in range(n, 0, -1):
    other = 0
    for j in range(i*2, n+1, i):
        if boll[j]: other+=1
    
    if a[i-1]==0:
        if other%2!=0: boll[i]+=1
    else:
        if other%2!=1: boll[i]+=1

ans = boll.count(1)
print(ans)
for i in range(1, n+1):
    if boll[i]: print(i)