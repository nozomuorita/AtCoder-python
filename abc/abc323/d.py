"""
・合成は、サイズの小さいスライムから行って良い -> サイズの小さいものを合成すると2倍のサイズのスライムになるため、小さいほうから考えればすべてを考慮して合成できるといえる
・heapqを用いて実装(最小値の取り出し)
・サイズxのスライムを合成すると、サイズ2*xのスライムが生成されるのでそれをheapqに入れて逐次取り出すことで小さいサイズから考えることができる
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush
n = int(input())
d = defaultdict(int)                    #  key: サイズ, value: スライムの数
slime = 0                               #  スライムの合計数

for i in range(n):
    s, c = map(int, input().split())
    slime += c
    d[s] += c
    
keys = list(d.keys())
keys.sort()
heapify(keys)                          #  サイズのリストをheapifyして小さいほうから取り出せるようにする

# keyがなくなるまで(すべてのサイズのスライムについて考慮するまで)
while keys:
    key = heappop(keys)                #  サイズの取り出し
    t = d[key]                         #  サイズkeyのスライムの数
    t2 = (t//2)                        #  サイズkeyのスライムを合成できる回数。2体で合成できるので、2で割った商の回数だけ合成できる
    
    if t2>0:
        # 減るスライム(サイズkey)
        d[key] -= t2*2                 #  1回の合成で2体使うので合成回数*2だけ減る
        slime -= t2*2                  #  スライムの総数も同様に減る
        
        # 増えるスライム(サイズ2*key)
        d[2*key] += t2                 #  合成回数だけスライムが生成される
        slime += t2                    #  総数も同様
        heappush(keys, 2*key)          # heapqに2*keyを入れて、次の合成候補とする
    
print(slime)