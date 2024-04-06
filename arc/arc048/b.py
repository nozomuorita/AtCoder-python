"""
・自分よりレートが高い人には負け
・自分よりレートが低い人には勝ち
・事前にレートの低い順に累積和を計算しておき、両方計算し、勝ちと負けに記録
・同レートは素直に勝ち、負け、引き分けの人数を数える
"""
from collections import defaultdict
n = int(input())
rh = []
d = defaultdict(lambda: [0, 0, 0])
for i in range(n):
    r, h = map(int, input().split())
    rh.append([r, h-1])
    d[r][h-1] += 1
    
keys = sorted(d.keys())
cum = [0]*(10**6)             # そのレートまでに何人いるのかの累積和
cum[keys[0]] = sum(d[keys[0]])
for i in range(1, len(keys)):
    cum[keys[i]] = cum[keys[i-1]] + sum(d[keys[i]])

ans = [[0, 0, 0] for _ in range(n)]
for i in range(n):
    # lose
    ans[i][1] += n - cum[rh[i][0]]                      # レートが真に高い人には負ける
    # win
    if rh[i][0]!=keys[0]:
        ans[i][0] += cum[rh[i][0]] - sum(d[rh[i][0]])   # レートが真に低い人には勝つ
    # same rate
    d[rh[i][0]][rh[i][1]] -= 1
    if rh[i][1]==0:
        ans[i][2] += d[rh[i][0]][0]
        ans[i][0] += d[rh[i][0]][1]
        ans[i][1] += d[rh[i][0]][2]
    elif rh[i][1]==1:
        ans[i][2] += d[rh[i][0]][1]
        ans[i][0] += d[rh[i][0]][2]
        ans[i][1] += d[rh[i][0]][0]
    else:
        ans[i][2] += d[rh[i][0]][2]
        ans[i][0] += d[rh[i][0]][0]
        ans[i][1] += d[rh[i][0]][1]
    d[rh[i][0]][rh[i][1]] += 1

for i in ans:
    print(*i)





# for i in range(n):
#     while idx<n and rh[idx][0]==rh[i][0]:
#         if idx==i:
#             idx += 1
#             continue
        
#         score1, score2 = janken(rh[i][1], rh[idx][1])
#         ans[i][score1] += 1
#         ans[idx][score2] += 1
        
#         idx += 1
#         if idx==n: break
    
#     ans[i][1] += n-idx

# print("-----------------")
# for i in ans:
#     print(*i)