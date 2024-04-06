s = input()
ans = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        if j+1==len(s): text=s[i:]
        else: text = s[i:j+1]
        
        ans.add(text)

print(len(ans))
print(ans)