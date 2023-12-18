n = list(map(int, input().split()))
ans = 0

while len(set(n))!=1:
    n.sort()
    if n[2]-n[0]>=2:
        n[0] += 2
    elif n[2]-n[0]==1:
        n[0] += 1
        n[1] += 1
    ans += 1

print(ans)
