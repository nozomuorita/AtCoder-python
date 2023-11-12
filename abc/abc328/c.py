n, q = map(int, input().split())
s = input()

# 累積和
d = [0, 0]
for i in range(1, n):
    if s[i]==s[i-1]: d.append(d[-1]+1)
    else: d.append(d[-1])
    
for i in range(q):
    l, r = map(int, input().split())
    ans = d[r]-d[l]
    print(ans)