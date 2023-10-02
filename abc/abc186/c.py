n = int(input())

ans = 0
for i in range(1, n+1):
    o = oct(i)
    if ('7' not in str(i)) and ('7' not in o):
        ans += 1
print(ans)