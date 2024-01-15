n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# dp[i]: [i番目の部屋までにかかる最短時間, どの部屋から来たか]
dp = [[10**18, -1]] * n
dp[0] = [0, -100]

for i in range(1, n):
    if i==1:
        if dp[i-1][0]+a[i-1]<dp[i][0]:
            dp[i] = [dp[i-1][0]+a[i-1], i-1]
    else:
        if dp[i-1][0]+a[i-1]<dp[i][0]:
            dp[i] = [dp[i-1][0]+a[i-1], i-1]
        if dp[i-2][0]+b[i-2]<dp[i][0]:
            dp[i] = [dp[i-2][0]+b[i-2], i-2]

ans = [n]
while dp[ans[-1]-1][1]!=-100:
    ans.append(dp[ans[-1]-1][1]+1)

print(len(ans))
print(*ans[::-1])