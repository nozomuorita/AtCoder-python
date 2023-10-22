n = int(input())
ng = [int(input()) for _ in range(3)]

if n in ng: exit(print('NO'))

# dp[i][j]: i回目の操作で数字をjとすることができるか(-1: できない、1: できる)
dp = [[-1]*(n+1) for _ in range(101)]
dp[0][n] = 1

for i in range(1, 101):
    for j in range(n, -1, -1):
        if dp[i-1][j]==1 and (j not in ng):
            if (j-1)>=0: dp[i][j-1] = 1
            if (j-2)>=0: dp[i][j-2] = 1
            if (j-3)>=0: dp[i][j-3] = 1
    if dp[i][0]==1: exit(print('YES'))
    
print('NO')
# for i in range(len(dp)): print(dp[i])

# for i in range(n, -1, -1):
#     if dp[i]==1 and (i not in ng):
#         if (i-1)>=0: dp[i-1] = 1
#         if (i-2)>=0: dp[i-2] = 1
#         if (i-3)>=0: dp[i-3] = 1
        
# print('YES') if dp[0]==1 else print('NO')
# print(dp)