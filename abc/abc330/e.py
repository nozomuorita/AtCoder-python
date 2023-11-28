from collections import defaultdict
from sortedcontainers import SortedList
n, q = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(int)
for i in a: d[i]+=1

mex = SortedList()    #  mex候補を何個か列挙しておく
idx = 0
while len(mex)<2*n:
    if d[idx]==0: mex.add(idx)
    idx+=1
    
for i in range(q):
    i, x = map(int, input().split())
    i -= 1

    #  dictを見てmexを更新
    d[a[i]] -= 1
    if d[a[i]]==0: mex.add(a[i])
    # if d[x]==0:
    mex.discard(x)
    d[x] += 1

    a[i] = x
    ans = mex.pop(0)   # 最小の値を出力
    print(ans)
    #print(mex[0])
    mex.add(ans)