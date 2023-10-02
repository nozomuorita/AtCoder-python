s = list(input())

ans = 1
for i in range(2, len(s)):
    for j in range(len(s)-i+1):
        s2 = s[j:j+i+1]
        s3 = list(reversed(s2))
        if s2==s3:
            if len(s2)>ans:
                ans = len(s2)
                
print(ans)