s = input()
cnt = [0]*30

for i in s:
    tmp = ord(i) - ord("a")
    cnt[tmp] += 1

ans = ""
mx = -1
for i in range(26):
    if cnt[i]>mx:
        ans = chr(ord("a")+i)
        mx = cnt[i]

print(ans)