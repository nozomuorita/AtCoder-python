n = int(input())
s = [input() for _ in range(n)]

ans = ""
for c in range(26):
    ch = chr(ord("a")+c)
    cnt = float("inf")
    
    for i in s:
        cnt = min(cnt, i.count(ch))
    
    ans += ch*cnt

print(ans)