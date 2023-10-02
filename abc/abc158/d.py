from collections import deque
s = deque(input())
Q = int(input())
f = False

for i in range(Q):
    q = list(map(str, input().split()))
    if int(q[0])==1:
        f = not(f)
    else:
        c = q[2]
        if int(q[1])==1:
            if f:
                s.append(c)
            else:
                s.appendleft(c)
        else:
            if f:
                s.appendleft(c)
            else:
                s.append(c)
    print(s)

if f:
    print(''.join(reversed(s)))
else:
    print(''.join(s))