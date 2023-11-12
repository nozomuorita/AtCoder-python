from collections import deque

s = input()
l = len(s)
q = deque()

for i in range(l):
    if s[i]!='C': q.append(s[i])
    else:
        if len(q)<2: q.append(s[i]); continue
        c1 = q.pop()
        c2 = q.pop()
        if c1=='B' and c2=='A': continue
        else:
            q.append(c2)
            q.append(c1)
            q.append(s[i])

ans = ''
while q:
    c = q.popleft()
    ans += c
print(ans)