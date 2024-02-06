from itertools import product
n = int(input())
s = input()

ans = 1<<60
c = list(product("ABXY", repeat=2))
for i in c:
    for j in c:
        L = i[0]+i[1]
        R = j[0]+j[1]
        idx, score = 0, 0
        while idx<n-1:
            if s[idx]+s[idx+1]==L or s[idx]+s[idx+1]==R:
                score += 1
                idx += 2
            else:
                score += 1
                idx += 1
        if idx==n-1: score+=1
        ans = min(ans, score)

print(ans)