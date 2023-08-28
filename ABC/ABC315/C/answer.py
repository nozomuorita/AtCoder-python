from collections import defaultdict
n = int(input())
fs = defaultdict(list)
mx = -1
mx_f = -1
for i in range(n):
    f, s = map(int, input().split())
    fs[f].append(s)
    if s>mx:
        mx = s
        mx_f = f

# 同じ味の場合
ans1 = -1
sorted_list = sorted(fs[mx_f], reverse=True)
if len(sorted_list)>1:
    ans1 = sorted_list[0] + (sorted_list[1]//2)

# 異なる味のとき
second_mx = -1
ans2 = -1
for key in list(fs.keys()):
    if key==mx_f:
        continue
    if max(fs[key])>second_mx:
        second_mx = max(fs[key])
        
ans2 = mx + second_mx
print(max(ans1, ans2))