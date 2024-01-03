from collections import deque
n = int(input())
a = [int(input()) for _ in range(n)]

def f(j):
    q = deque(sorted(a))
    lst = []
    for i in range(n):
        if j==0:
            v = q.pop()
            lst.append(v)
        else:
            v = q.popleft()
            lst.append(v)
        j = int(not(j))
    
    lst.insert(0, lst.pop())
    score = 0
    for i in range(n-1):
        score += abs(lst[i]-lst[i+1])
    return score

ans = max(f(0), f(1))
print(ans)