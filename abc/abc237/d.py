from collections import deque
n = int(input())
s = list(input())

a = deque()
a.append(n)

for i in range(n-1, -1, -1):
    if s[i] == 'L':
        a.append(i)
    else:
        a.appendleft(i)
    #print(a, s[i-1])
        
print(*a)