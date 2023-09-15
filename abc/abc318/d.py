from collections import defaultdict

n = int(input())
visited = [False] * n
ans = -1

g = defaultdict(int)
for i in range(n-1):
    tmp = list(map(int, input().split()))
    tmp_n = i+1
    for j in tmp:
        g[(i, tmp_n)] = j
        tmp_n += 1
print(g)
    
