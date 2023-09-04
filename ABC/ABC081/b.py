n = int(input())
a = list(map(int, input().split()))

ans = 0
while 1:
    f = True
    for i in range(n):
        if a[i]%2 != 0:
            f = False
            break
        else:
            a[i] //= 2
    if f:
        ans += 1
    else:
        break

print(ans)