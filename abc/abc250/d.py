"""
・素数(p or q)がとりうる最大値を求め、事前に素数を列挙する
・p<qであるため、qの最大値がとりうる最大の素数となる
・1<=pq**3<=nより、(1/p)**(1/3)<=q<=(n/p)**(1/3)となり、(n/p)**(1/3)以下の素数を列挙すればよいとなる → エラトステネスの篩で列挙
・列挙した素数を一つずつループで回し、qとする
・このとき、とりうるpの値の最大値は1/q**3<=p<=n/q**3より、n/q**3である
・このpを二分探索して探す(pのとりうる最大値がn以下ならば、それ以下の素数をpとしても成り立つ)
・注意: p<qという制約があるため、qの値も二分探索してインデックスを取得する
・最大のpのインデックスがqのインデックス未満ならば、pのインデックス以下はすべて成立するため、答えに足す
・最大のpのインデックスがqのインデックスよりも大きい場合、qより大きい部分はダメであり、qのインデックス未満の素数について成立する
・ゆえに、qのインデックス未満の素数の個数を答えに足す
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right
def eratosthenes_sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, n+1):
        if is_prime[p]:
            for q in range(2*p, n+1, p):
                is_prime[q] = False
    return is_prime

def ceil_div(x, y): return -(-x//y)

n = int(input())
mx_q = ceil_div(n**(1/3), 2**(1/3))     # とりうる素数の最大値
mx = int(mx_q)

if n==1: exit(print(0))                 # n=1のときは0

#  素数列挙
lst = eratosthenes_sieve(mx)
prime = []
for i in range(2, mx+1):
    if lst[i]: prime.append(i)

ans = 0
for i in range(len(prime)):
    q = prime[i]                      #  qを定義
    x = n/(q**3)                      #  とりうるpの最大値
    idx_q = bisect_right(prime, q)    #  qのインデックス
    idx_p = bisect_right(prime, x)    #  とりうるpの最大値のインデックス
    
    if idx_p<idx_q: ans+=idx_p        #  最大のpのインデックスがqのインデックス未満なら、すべて成立
    else: ans+=idx_q-1                #  最大のpのインデックスがqのインデックス以上なら、qのインデックス未満について成立
        
print(ans)