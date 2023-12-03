"""二次元いもす法"""
n = int(input())
paper = [[0]*1001 for _ in range(1001)]

for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    paper[lx][ly] += 1
    paper[rx][ly] -= 1
    paper[lx][ry] -= 1
    paper[rx][ry] += 1

for i in range(1001):
    for j in range(1, 1001):
        paper[i][j] += paper[i][j-1]
        
for i in range(1001):
    for j in range(1, 1001):
        paper[j][i] += paper[j-1][i]

ans = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        ans[paper[i][j]] += 1
    
for i in ans[1:]: print(i)