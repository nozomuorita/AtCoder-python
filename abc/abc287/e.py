"""
・各文字列について最大のLCPとなるのはソートした時に隣接する文字列のどっちか
・ソートして隣り合うもののみLCPを計算する
"""
n = int(input())
s = [[input(), _] for _ in range(n)]    #  [文字列, 文字列のインデックス]
s.sort()

ans = [0]*n                             #  ans[i]: i番目の文字列の最大LCP
for i in range(n-1):
    score = 0
    for j in range(min(len(s[i][0]), len(s[i+1][0]))):   #  二つのうち、長さが小さいほうだけ見る
        if s[i][0][j]==s[i+1][0][j]: score+=1
        else: break                                      #  j番目の文字が異なるならそこまで
    
    ans[s[i][1]] = max(ans[s[i][1]], score)              #  文字列のインデックスのところにscoreを更新する
    ans[s[i+1][1]] = max(ans[s[i+1][1]], score)
    
for i in ans: print(i)