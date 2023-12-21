from collections import deque
s = input()
rev = False

ans = deque()
for i in s:
    if i=="R": rev=not(rev); continue
    if rev:
        if ans:
            pre = ans.popleft()
            if i!=pre: ans.appendleft(pre); ans.appendleft(i)
        else: ans.appendleft(i)
    else:
        if ans:
            pre = ans.pop()
            if i!=pre: ans.append(pre); ans.append(i)
        else: ans.append(i)
        
if rev:
    while ans: print(ans.pop(), end="")
else:
    while ans: print(ans.popleft(), end="")