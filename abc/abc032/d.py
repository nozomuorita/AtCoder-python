from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict
n, W = map(int, input().split())
v, w = [], []
for i in range(n):
    _ = list(map(int, input().split()))
    v.append(_[0]); w.append(_[1])

# データセット１(集合を二つに分け、二分探索)
if n<=30:
    ans = 0
    s1, s2 = [], []
    
    for i in range(2**(n//2)):
        tw, tv = 0, 0
        for j in range(n//2):
            if i>>j & 1:
                tv += v[j]
                tw += w[j]
        s1.append([tw, tv])
    
    s1.sort()
    del_lst, mx = [], s1[0][1]
    for i in range(1, len(s1)):
        if s1[i][1]<=mx: del_lst.append(s1[i])
        else: mx=s1[i][1]
    
    for i in del_lst:
        s1.remove(i)
    
    s1_w = [i[0] for i in s1]
    s1_v = [i[1] for i in s1]
    
    for i in range(2**(n-(n//2))):
        tw, tv = 0, 0
        for j in range(n-(n//2)):
            if i>>j & 1:
                tv += v[j+(n//2)]
                tw += w[j+(n//2)]
        s2.append([tw, tv])
    s2.sort()
    
    for i in range(len(s2)):
        tw = W - s2[i][0]
        idx = bisect_right(s1_w, tw) - 1
        if idx==-1: continue
        
        score = s2[i][1] + s1_v[idx]
        ans = max(ans, score)
    
    exit(print(ans))

# データセット２(重さでDP)
mx_w = max(w)
if mx_w<=1000:
    # dp[i][j]: i番目の品まで選んで、重さがjとなるときの最大価値
    dp = [[-1]*(sum(w)+1) for i in range(n+1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(sum(w)+1):
            if dp[i][j]!=-1:
                # 選ぶとき
                dp[i+1][j+w[i]] = max(dp[i+1][j+w[i]], dp[i][j]+v[i])
                # 選ばない
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    
    ans = 0
    for i in range(sum(w)+1):
        if i<=W: ans = max(ans, dp[-1][i])
    exit(print(ans))

# データセット３(価値でDP)
mx_v = max(v)
if mx_v<=1000:
    # dp[i][j]: i番目の品物まで選んで、価値の総和がjとなるときの最小重さ
    dp = [[10**18]*(sum(v)+1) for i in range(n+1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(sum(v)+1):
            if dp[i][j]!=10**18:
                # 選ぶとき
                dp[i+1][j+v[i]] = min(dp[i+1][j+v[i]], dp[i][j]+w[i])
                # 選ばないとき
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    
    ans = 0
    for i in range(sum(v)+1):
        if dp[-1][i]<=W: ans=i
    exit(print(ans))