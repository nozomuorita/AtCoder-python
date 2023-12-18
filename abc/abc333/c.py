import sys
sys.setrecursionlimit(100000000)
n = int(input())

mx = 112222222233
lst = []
def dfs(i):
    print(i)
    if len(i)==3: 
        lst.append(sum(i))
        return
    for j in range(1, 16):
        tmp = int("1"*j)
        if sum(i+[tmp])>mx: continue
        dfs(i+[tmp])

dfs([])
lst = list(set(lst))
lst.sort()
print(lst[n-1])
