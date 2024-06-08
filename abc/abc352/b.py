s = input()
t = input()

idx = 0
ans = []
for i in range(len(t)):
    if s[idx]==t[i]:
        ans.append(i+1)
        idx += 1
    if idx==len(s): break

print(*ans)