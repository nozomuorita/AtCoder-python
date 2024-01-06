h, w, n = map(int, input().split())
grid = [[0]*(w+2) for _ in range(h+2)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[a][d+1] -= 1
    grid[c+1][b] -= 1
    grid[c+1][d+1] += 1

for i in range(1, h+2):
    for j in range(1, w+2):
        grid[i][j] += grid[i][j-1]
        
for i in range(1, h+2):
    for j in range(1, w+2):
        grid[i][j] += grid[i-1][j]

for i in range(1, h+1):
    print(*grid[i][1:w+1])