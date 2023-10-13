# 8の倍数は下3桁が8の倍数かどうか
from collections import defaultdict

s = input()
c = [False] * 10

# 各数字の出現回数を記録
d = defaultdict(int)
for i in s:
    d[i] += 1
    
# sが何桁か確認(1, 2, 3, 4以上)
l = len(s)
    
    
# 3桁以下で8の倍数であるものを列挙
eight = set()
n = 8

# sが1桁や2桁の場合は、1, 2桁までの倍数を列挙
if l >= 3:
    div = 1000
    l = 3
else:
    div = 10 ** (l)
    l = l
    
eight.add('8'.zfill(l))

# 4桁未満である間繰り返す
while (n//div<=0):
    eight.add(str(n).zfill(l))
    n += 8
    
# 列挙した8の倍数について、その数字が存在するか判定
# 注意：先頭が0になってしまわないかを確認
for e in eight:
    d2 = defaultdict(int)
    if l >= 3:
        d2[e[0]] += 1
        d2[e[1]] += 1
        d2[e[2]] += 1

        # e(8の倍数)を作ることができるなら、
        if (d[e[0]]>=d2[e[0]]) and (d[e[1]]>=d2[e[1]]) and (d[e[2]]>=d2[e[2]]):
            # 残りが0のみでないか確認
            f = True
            for key in list(d.keys()):
                if key=='0':
                    continue

                if (key==e[0]) and (d[key]-d2[key]>0):
                    print('Yes')
                    exit()
                elif (key==e[1]) and (d[key]-d2[key]>0):
                    print('Yes')
                    exit()
                elif (key==e[2]) and (d[key]-d2[key]>0):
                    print('Yes')
                    exit()
                else:
                    if d[key]>0:
                        print('Yes')
                        exit()
                        
    elif l == 2:
        d2[e[0]] += 1
        d2[e[1]] += 1
        
        # e(8の倍数)を作ることができるなら、
        if (d[e[0]]==d2[e[0]]) and (d[e[1]]==d2[e[1]]):
            print('Yes')
            exit()

    else:
        d2[e[0]] += 1
        if d[e[0]]==d2[e[0]]:
            print('Yes')
            exit()

print('No')