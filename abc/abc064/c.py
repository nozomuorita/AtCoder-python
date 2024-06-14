from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
free = 0

for i in a:
    if i < 400:
        d['gray'] += 1
    elif i < 800:
        d['brown'] += 1
    elif i < 1200:
        d['green'] += 1
    elif i < 1600:
        d['light-blue'] += 1
    elif i < 2000:
        d['blue'] += 1
    elif i < 2400:
        d['yellow'] += 1
    elif i < 2800:
        d['orange'] += 1
    elif i < 3200:
        d['red'] += 1
    else:
        free += 1

num = len(list(d.keys()))
ans_mx = num
ans_mn = num

if free > 0:
    if num == 0:
        ans_mx = free
        ans_mn = 1
    else:
        ans_mx += free

print(ans_mn, ans_mx)