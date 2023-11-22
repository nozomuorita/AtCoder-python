from collections import deque
s = input()

box = set()
q = deque()

for i in s:
    if i=="(": q.append(i)
    elif i==")":
        k = -1
        while k!=0:
            v = q.pop()
            if v==")": k-=1
            elif v=="(": k+=1
            else: box.discard(v)
    else:
        if i in box: exit(print('No'))
        else: box.add(i); q.append(i)
        
print('Yes')