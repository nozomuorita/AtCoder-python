from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1
    
d2 = sorted(d.items(), reverse=True)
h = []   # 2本以上ある辺を2つ取得(大きいものから)
h2 = []  # 4本以上ある(正方形を作れる)ものを1つ取得(大きいものから)
for i in d2:
    if (len(h)==2) and (len(h)==1):
        break
    if (len(h2)<1) and (i[1]>=4):
        h2.append(i[0])
    if (len(h)<2) and (i[1]>=2):
        h.append(i[0])

if len(h)<2:
    ans1 = 0
else:
    ans1 = h[0] * h[1]
if len(h2)==0:
    ans2 = 0
else:
    ans2 = h2[0] ** 2
print(max(ans1, ans2, 0))