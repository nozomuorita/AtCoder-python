t = input()
n = int(input())
a = []
s = []
for i in range(n):
    tmp = list(map(str, input().split()))
    a.append(int(tmp[0]))
    s.append(tmp[1:])
    
# dp[i][j]: i番目まで見て、j文字目まで埋めることができるか
dp = [[(False, -1)]*(len(t)+1) for _ in range(n+1)]
dp[0][0] = (True, 0)

for i in range(n):
    for j in range(len(t)+1):
        if dp[i][j][0]:
            f = dp[i][j][1]
            if dp[i+1][j][0]==False: dp[i+1][j] = (True, f)
            elif dp[i+1][j][1]>f: dp[i+1][j]=(True, f)
            for k in s[i]:
                if k==t[j:j+len(k)]:
                    if dp[i+1][j+len(k)][0]==False: dp[i+1][j+len(k)]=(True, f+1)
                    elif dp[i+1][j+len(k)][1]>(f+1): dp[i+1][j+len(k)]=(True, f+1)

print(dp[-1][-1][1])

#for i in dp: print(i)