N = int(input())

# Nの何bit目が1であるかを格納
flag = []
for i in range(60):
    
    # 1を i 桁だけ左シフトした値とNのアンドが0以上ならば
    # 1, 10, 100...と見ていっている
    # Nの i bit目が1ならば，ifの中に入る
    if N & (1 << i):
        flag.append(i)
        
l = len(flag)

# l はNを2進数にした時の1の数
# Nの1があるところそれぞれについて1にするか0にするかの2通りなので，パターン数は2のl乗だけある
# flagの各要素を選ぶかどうかをfor文でパターン化
# 選ぶなら１０進数にして足していく
for bit in range(1 << l):
    now = 0
    for i in range(l):
        if bit & (1 << i):
            now += (1 << flag[i])
    print(now)
    
# 別解(combination)
# from itertools import combinations

# n = int(input())
# keta = len(bin(n))-2                     #  2進数での桁数

# n = bin(n)[2:]
# one_set = set()                          #  1の桁を格納
# for i in range(keta):
#     if n[keta-i-1]=="1": one_set.add(i)

# ans = [0]
# for i in range(1, len(one_set)+1):       #  1の数が1個から(nでの1の数)まで
#     s = combinations(list(one_set), i)   #  nにおいて、1である桁からi個1とする場所を選ぶ
#     for j in s:
#         number = 0
#         for k in j: number+=2**k         #  選んだ場所を加算
#         ans.append(number)

# ans.sort()
# for i in ans: print(i)