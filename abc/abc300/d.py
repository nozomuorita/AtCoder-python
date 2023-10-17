"""
・c=(n/(a**2)*b)**0.5であるため、cはa=2、b=3としたときの値以下の素数であるといえる
・よって、x=int((n/(2**2)*3)**0.5)=(n/12)**0.5以下の素数を列挙する。
・列挙した素数について、a、bをfor文で回し、固定する。
・すると、上のc=の式より、cが満たす上限値xが求まる(=nとなるcの値)。
・その値を列挙した素数から二分探索する
・b以上であり、x以下である素数についてはn以下という条件を満たすため、二分探索して得たインデックスからb以上である素数の個数をansに足していく
・a、bを固定したときに、求めたcの上限値がa<b<cを満たさないなら、それ以降のa、bについてはすべて満たさないためbreakする
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right
import math
n = int(input())

# エラトステネスの篩
def prime(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

# cとして考えられる最大の値は、a=2、b=3とした場合である。
# よって、a=2、b=3としたときにnとなるcの値=(n/12)**0.5以下の素数を列挙すればよい
n2 = int((n/12)**0.5)
prime = prime(n2)

# 素数判定を基に, 素数リストを作成
prime_list = []
for i in range(n2 + 1):
    if prime[i]:
        prime_list.append(i)

ans = 0
# a, bをループで回す
for i in range(len(prime_list)):
    for j in range(i+1, len(prime_list)-1):
        a = prime_list[i]
        b = prime_list[j]
        #  a, bを固定すると、与式=nが満たすべきcの値xが定まる
        #  ゆえに、b以上x以下を満たす素数は、すべて条件を満たす
        x = int((n/((a**2)*b))**0.5)
        if (a**2)*b*(prime_list[j+1]**2)>n: break    #  もし、bの次の素数をcとしたときにnを超えるならそれ以降はすべて満たさないのでbreak
        # if x<=b: break
        idx = bisect_right(prime_list, x)            #  二分探索
        ans += idx-(j+1)                             #  b以上であり、x以下の素数の数だけ足す
        
print(ans)