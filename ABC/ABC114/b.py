s = input()

ans = 10**9
for i in range(0, len(s)-2):
    n = 100*int(s[i]) + 10*int(s[i+1]) + int(s[i+2])
    if abs(753-n) < ans:
        ans = abs(753-n)

print(ans)