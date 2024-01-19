"""
・シンプルに各駅について、今の時刻以降に発車する時間(t>=nowを満たす最小のt)を探し、更新していく
・駅iでは、時刻s[i]+xf[i](x=0, 1, 2...)に電車が出る
・今の時刻をtとすると、t以降に発車する電車は、t>=s[i]+xf[i]である。
・これを満たす最小のtを求め、この電車に乗るとする
・x>=(t-s[i])/f[i]を満たす最小のxを求め、上式に代入することで駅iをいつ出発するかが求まる
"""
def ceil_div(x, y): return -(-x//y)
n = int(input())
c, s, f = [], [], []
for i in range(n-1):
    _ = list(map(int, input().split()))
    c.append(_[0])
    s.append(_[1])
    f.append(_[2])

for i in range(n-1):
    time = s[i] + c[i]                          # 出発点ではs[i]の電車に乗れるので、s[i]+c[i]かけて次の駅にいく
    for j in range(i+1, n-1):                   # i+1以降を計算
        if s[j]>=time: mn_t=0                   # もし、駅jに到着する時間がs[i](最初に発車する時間)より早いならs[i]に乗る
        else: mn_t = ceil_div(time-s[j], f[j])  # そうでないなら、何本目に出発する電車か計算
        time = s[j] + (mn_t * f[j]) + c[j]      # timeを更新
    
    print(time)

print(0)