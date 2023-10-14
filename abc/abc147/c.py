"""
・n<=15なので、bit全探索できる
・1が立っている人を正直者であるとして、矛盾しないか判定
・矛盾しないならば、最大値が更新されるか判定
"""

n = int(input())
xy = []

for i in range(n):
    a = int(input())
    tmp = [list(map(int, input().split())) for _ in range(a)]
    xy.append(tmp)
    
ans = 0
for i in range(2**n):
    q = []                       #  正直者であると仮定する人の番号を入れる
    honest = 0                   #  正直者の人数(1が立っている数)
    c = [0]*n                    #  証言による各人の状態(0: 不親切、1: 正直者)
    f = True                     # 矛盾しているかどうかのフラグ
    for j in range(n):
        # 1が立っている人を「正直者」、0が立っている人を「不親切」と仮定する(cの状態を設定)
        if (i>>j) & 1:
            honest += 1
            c[j] = 1
            q.append(j)
    
    # 正直者である人の証言を一つずつ見ていき、上で設定したcと異なるならば、矛盾。よって成立しない
    for j in q:
        if f:
            for x, y in xy[j]:
                x -= 1
                if c[x]!=y:
                    f = False
                    break
    
    # 矛盾しないなら最大値を比較・更新
    if f: ans=max(ans, honest)
    
print(ans)