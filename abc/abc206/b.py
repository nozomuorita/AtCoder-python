n = int(input())
ans = 1
while 1:
    if ans*(ans+1) >= 2*n:
        break
    ans += 1
print(ans)