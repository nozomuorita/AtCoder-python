s = input()
ans1 = 0
f = True
for i in range(len(s)):
    if f:
        if s[i]=="1": ans1+=1
    else:
        if s[i]=="0": ans1+=1
    f = not(f)

ans2 = 0
f = True
for i in range(len(s)):
    if f:
        if s[i]=="0": ans2+=1
    else:
        if s[i]=="1": ans2+=1
    f = not(f)

print(min(ans1, ans2))