from collections import defaultdict
n = int(input())
d = defaultdict(lambda: False)
cnt = 0

for i in range(2, 10**5+1):
    if i**2>n: break
    for j in range(2, 10**5+1):
        p = i**j
        if p<=n:
            if d[p]==False:
                cnt += 1
                d[p] = True
        else:
            break

ans = n - cnt
print(ans)