n = int(input())
s = input()
k = int(input())

ans = ""
ss = s[k-1]

for i in s:
    if i==ss: ans+=i
    else: ans+="*"
    
print(ans)