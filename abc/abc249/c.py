from collections import defaultdict
n, k  = map(int, input().split())
s = [input() for i in range(n)]

ans = 0

# bit全探索
for i in range(2**n):
    d = defaultdict(int)
    num = 0 # k個登場する文字の種類
    for j in range(n):
        if ((i >> j) & 1):
            #num += 1
            for m in s[j]:
                d[m] += 1
    
    for i in list(d.keys()):
        if d[i] == k:
            num += 1
    if ans < num:
        ans = num

print(ans)