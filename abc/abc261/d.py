"""
・dp
・dp[i][j]: i日目まで考えて、カウンタがjであるときの最大値
・最初は全部0で初期化しておく
・初期値: dp[0][0]=0
・dpテーブルの更新
・カウンタが0(j=0)のとき、最大値はひとつ前(=i-1)の時点での最大値
・j!=0のとき、すなわち表が出た時は、i-1枚目までの時点においてカウンタがj-1であるときの最大値(dp[i-1][j-1])にxを足したもの
・ただし、カウンタをjにすることが不可能(1回目の時点でカウンタを3にするなど)の場合は、-1とする
・加えて、jがボーナスの日であるなら、ボーナス分を足す
"""

from collections import defaultdict
n, m = map(int, input().split())
x = list(map(int, input().split()))
d = defaultdict(int)

for i in range(m):
    c, y = map(int, input().split())
    d[c] = y                                         #  連続ボーナス

# dp[i][j]: i日目まで考えて、カウントがjであるときの最大値
dp = [[-1]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(n+1):
        if j==0: dp[i][j] = max(dp[i-1])             #  jが0であるなら、ひとつ前の時点での最大値をとる
        else:
            if dp[i-1][j-1]==-1: continue            #  もし、i-1枚目の時点でカウンタをj-1にすることができない場合(=-1)は、実現不可能なので飛ばす
            dp[i][j] = dp[i-1][j-1] + x[i-1]         #  実現可能なら、xを足したものとする
        
        dp[i][j] += d[j]                             #  もし、カウンタをjとしたときがボーナスならボーナス分足す。
        
print(max(dp[-1]))