# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y)

# main code ------------------------------------------------------------------------------------
# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y) 

# main code ------------------------------------------------------------------------------------
# @nzm_ort
# https://github.com/nozomuorita/atcoder-workspace-python

# import module ------------------------------------------------------------------------------
from collections import defaultdict, deque, Counter
import math
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import bisect
import sys
# sys.setrecursionlimit(100000000)
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y) 

# main code ------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    n = int(input())
    n_bin = bin(n)[2:]   # 2進数表現
    length = len(n_bin)  # 2進数の長さ

    # 6以下なら存在しないため、-1を出力
    if n<=6:
        print(-1)

    else:
        # 1の個数をカウント
        one = n_bin.count('1')

        # 1の数が3こならば、その数を出力
        if one==3:
            print(n)

        # 1が3個以上であれば、上位3つの1を残して他を0にする
        if one > 3:
            ans = ''
            cnt = 0 # 1を何個とったか
            for j in range(length-1, -1, -1):
                if ((n>>j) & 1) and (cnt < 3):
                    ans += '1'
                    cnt += 1
                else:
                    ans += '0'
            print(int(ans, 2))

        # 1の数が1個の場合 → 最上位桁を0にして、その下3つを1にする
        if one==1:
            ans = ('1'*3) + ('0'*(length-1-3))
            print(int(ans, 2))

        # 1の数が2個のとき
        if one==2:
            # 下位の1がどの位置にあるか確認
            first = 0
            for j in range(length):
                if (n>>j) & 1:
                    first = j
                    break
            # jが2以上の時、下のほうの桁の1を0としてその下に1を2つつける
            if first >= 2:
                ans = n_bin
                ans = ans[:-(j+1)]
                ans += '0'
                ans += '11'
                ans += '0' * (length-len(ans))
                print(int(ans, 2))

            # 最上位桁を0としてその下に1を二つ入れる
            else:
                cnt = 0
                first = 0
                ans = ''
                for j in range(length-1, -1, -1):
                    if ((n>>j)&1) and (first==0):
                        first += 1
                        ans += '0'
                    elif ((n>>j)&1) and (cnt<3):
                        ans += '1'
                        cnt += 1
                    elif (not((n>>j)&1)) and (cnt<3):
                        ans += '1'
                        cnt += 1
                    else:
                        ans += '0'
                print(int(ans, 2))