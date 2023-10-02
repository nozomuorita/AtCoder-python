n = int(input())
s = list(input())

ans = -1
for i in range(len(s)-2):
    if s[i]=='A' and s[i+1]=='B' and s[i+2]=='C':
        ans = i+1
        break
    
print(ans)