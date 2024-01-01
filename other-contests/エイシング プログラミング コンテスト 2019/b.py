n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

q = [0, 0, 0]
for i in range(n):
    if p[i]<=a: q[0]+=1
    elif p[i]<=b: q[1]+=1
    else: q[2]+=1

print(min(q))