s = input()
f = True
ans = ""
for i in s:
    if i=="|": f=not(f)
    else:
        if f: ans += i

print(ans)