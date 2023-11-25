"""
・DP
"""
from collections import defaultdict
n = int(input())
d = defaultdict(list)
mx = -1
for i in range(n):
    lst = list(map(int, input().split()))
    d[lst[0]].append(lst[1:])
    if lst[0]>mx: mx=lst[0]

#  dp[i][j]: 時刻iに座標jにいるときの最大値
dp = [[-1]*5 for _ in range(mx+1)]
dp[0][0] = 0

for i in range(mx):
    for j in range(5):
        if dp[i][j]==-1: continue

        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        if j>0: dp[i+1][j-1]=max(dp[i+1][j-1], dp[i][j])
        if j<4: dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j])
        
        for lst in d[i+1]:
            if lst[0]==j-1: dp[i+1][j-1]=max(dp[i+1][j-1], dp[i][j]+lst[1])
            if lst[0]==j: dp[i+1][j]=max(dp[i+1][j], dp[i][j]+lst[1])
            if lst[0]==j+1: dp[i+1][j+1]=max(dp[i+1][j+1], dp[i][j]+lst[1])

print(max(dp[-1]))