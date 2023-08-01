n, x = map(int, input().split())
a = list(map(int, input().split()))

a.insert(0, 0)
f = True
ans = 1
knew = set()
knew.add(x)

while f:
    if a[x] in knew:
        break
    else:
        ans += 1
        knew.add(a[x])
        x = a[x]
    
    if ans == n:
        break

print(ans)