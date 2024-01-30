"""料理Aを何人分作るかを考える"""
n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ok = True
ans = 0
for i in range(2*(10**6)):
    tmp = float("inf")
    for j in range(n):
        if b[j]!=0:
            tmp = min(tmp, q[j]//b[j])

    ans = max(ans, i+tmp)

    for j in range(n):
        q[j] -= a[j]

    for j in range(n):
        if q[j]<0:
            ok = False
            break
    if ok==False:
        break

print(ans)