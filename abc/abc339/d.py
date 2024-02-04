from collections import deque
n = int(input())
s = [input() for _ in range(n)]

q = deque()
P = []
for i in range(n):
    for j in range(n):
        if s[i][j]=="P": P.append((i, j))
        
q.append((P[0][0], P[0][1], P[1][0], P[1][1], 0))
# dist[i][j][k][l]: player1:(i, j), player2:(k, l)での距離
dist = [[[[-1]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
dist[P[0][0]][P[0][1]][P[1][0]][P[1][1]] = 0

while q:
    ai, aj, bi, bj, d = q.popleft()
    for d1, d2 in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        # player1
        if 0<=ai+d1<n and 0<=aj+d2<n and s[ai+d1][aj+d2]!="#":
            ai2 = ai+d1
            aj2 = aj+d2
        else:
            ai2 = ai
            aj2 = aj
        # player2
        if 0<=bi+d1<n and 0<=bj+d2<n and s[bi+d1][bj+d2]!="#":
            bi2 = bi+d1
            bj2 = bj+d2
        else:
            bi2 = bi
            bj2 = bj

        if ai2==bi2 and aj2==bj2:
            exit(print(d+1))
        if dist[ai2][aj2][bi2][bj2]==-1:
            dist[ai2][aj2][bi2][bj2] = dist[ai][aj][bi][bj] + 1
            q.append((ai2, aj2, bi2, bj2, d+1))

print(-1)        