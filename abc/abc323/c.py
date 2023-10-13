"""
・現時点で最高得点なら、1問も解かなくてよい
・それ以外は、解いてない問題で配点の高いものから最高得点を超えるまで解いていく
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [input() for _ in range(n)]

score = []                            #  現時点でのスコア
unsolve = [[] for _ in range(n)]      #  まだ解いてない問題
for i in range(n):
    tmp = s[i]
    tmp_s = i+1
    for j in range(len(tmp)):
        if tmp[j]=='o':
            tmp_s += a[j]
        else:
            unsolve[i].append(a[j])
            
    score.append(tmp_s)

mx = max(score)                      #  現時点での最高スコア

for i in range(n):
    if score[i]==mx:                 #  最高スコアの人は1問も解く必要はない
        print(0)
        continue
    
    tmp = score[i]                   # それ以外は、unsolveの問題を得点の高いほうから選択
    ans = 0
    us = unsolve[i]
    us.sort(reverse=True)
    for k in us:
        tmp += k
        ans += 1
        if tmp>mx:                  # 最高得点を超えたなら出力
            break
    print(ans)