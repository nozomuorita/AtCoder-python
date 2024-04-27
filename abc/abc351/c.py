from collections import deque
n = int(input())
a = list(map(int, input().split()))

q = deque()
for i in range(n):
    q.append(a[i])
    while 1:
        if len(q)<=1: break
        
        ball1 = q.pop()
        ball2 = q.pop()
        if ball1!=ball2:
            q.append(ball2)
            q.append(ball1)
            break
        else:
            q.append(ball1+1)

print(len(q))