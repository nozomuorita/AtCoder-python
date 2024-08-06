n, x, y = map(int, input().split())
stone = [[0, 0] for _ in range(n+1)] # (red, blue)
stone[n][0] = 1

for i in range(n, 1, -1):
    for j in range(2):
        if j==0:
            stone[i-1][0] += stone[i][j]
            stone[i][1] += x * stone[i][j]
        else:
            stone[i-1][0] += stone[i][j]
            stone[i-1][1] += y * stone[i][j]

print(stone[1][1])
