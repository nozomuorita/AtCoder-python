import sys
sys.setrecursionlimit(100000000)
h, w = map(int, input().split())
s = [input() for _ in range(h)]

snuke = 'snuke'
visited = [[False]*w for _ in range(h)]

def dfs(i, j, n):
    visited[i][j] = True
    if (i==h-1) and (j==w-1):
        if s[i][j]==snuke[n]:
            print('Yes')
            exit()

    else:
        if s[i][j] == snuke[n]:
            for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if (0<=i2<h) and (0<=j2<w):
                    if (s[i2][j2]==snuke[(n+1)%5]) and (not(visited[i2][j2])):
                        dfs(i2, j2, (n+1)%5)

dfs(0, 0, 0)

print('No')