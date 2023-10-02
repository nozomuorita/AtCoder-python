n, m = map(int, input().split())
s = input()
t = input()

ans = 3
if s==t:
    print(0)
    exit()

if t[:n]==s and t[-n:]==s:
    ans = 0
elif t[:n]==s and t[-n:]!=s:
    ans = 1
elif t[:n]!=s and t[-n:]==s:
    ans = 2
else:
    ans = 3
print(ans)