from itertools import permutations
abcde = [int(input()) for _ in range(5)]

ans = float("inf")
p = permutations(range(5), 5)
for _p in p:
    t = 0
    for i in range(len(_p)):
        t += abcde[_p[i]]
        if i==4:
            ans = min(ans, t)
            continue
        while 1:
            if t%10==0: break
            t += 1
        
print(ans)