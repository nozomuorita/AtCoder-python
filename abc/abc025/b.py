n, a, b = map(int, input().split())
pos = 0
for i in range(n):
    s, d = map(str, input().split())
    d = int(d)
    d = min(d, b)
    d = max(d, a)
    if s=="East":
        pos -= d
    else:
        pos += d

if pos==0:
    print(0)
elif pos<0:
    print(*["East", abs(pos)])
else:
    print(*["West", pos])