s = input()

ans = 0
for i in range(len(s)):
    t = 0
    idx = 0
    while (i+idx)<len(s):
        if s[i+idx] in 'ACGT':
            t += 1
            idx += 1
        else:
            break
    ans = max(ans, t)
    
print(ans)