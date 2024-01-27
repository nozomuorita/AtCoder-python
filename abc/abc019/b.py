s = input()
ans = ""
cnt = 1

for i in range(len(s)-1):
    if s[i]==s[i+1]: cnt+=1
    else:
        ans += s[i] + str(cnt)
        cnt = 1

ans += s[-1] + str(cnt)
print(ans)