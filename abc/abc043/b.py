s = input()
ans = ""

for i in s:
    if i!="B":
        ans += i
    else:
        if len(ans)>0: ans=ans[:-1]

print(ans)