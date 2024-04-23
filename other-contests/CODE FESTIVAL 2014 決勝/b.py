s = input()
f = True
ans = 0
for i in s:
    if f:
        ans += int(i)
    else:
        ans -= int(i)
    f = not(f)
print(ans)