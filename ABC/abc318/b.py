n = int(input())

grid = [[False]*101 for i in range(101)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    for x in range(a, b):
        for y in range(c, d):
            grid[x][y] = True

ans = 0
for i in grid:
    ans += i.count(True)
print(ans)