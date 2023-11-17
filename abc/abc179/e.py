n, x, m = map(int, input().split())
an = x

ans = x
lst = [x]
if n==1: exit(print(x))
for i in range(n-1):
    an = (an**2)%m
    if an in lst: break
    ans += an
    lst.append(an)

if i==(n-2): exit(print(ans))

j = lst[lst.index(an):]
s = sum(j)
t = n-i-1
ans += (t//len(j)) * s
ans += sum(j[:t%len(j)])
print(ans)