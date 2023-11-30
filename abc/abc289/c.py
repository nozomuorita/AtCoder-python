"""bit全探索"""
n, m = map(int, input().split())
s = []
for i in range(m):
    c = int(input())
    a = set(map(int, input().split()))
    s.append(a)

ans = 0
for i in range(2**m):
    exist = [False]*n
    for j in range(m):
        if i>>j & 1:
            for k in range(1, 11):
                if k in s[j]: exist[k-1]=True
    
    if all(exist): ans+=1

print(ans)