x = input()
x = x.lower()
ans = ''
for i in range(len(x)):
    if i==0:
        ans += x[i].upper()
    else:
        ans += x[i]
print(ans)