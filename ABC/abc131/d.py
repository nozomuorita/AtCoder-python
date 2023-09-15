n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append([b, a])
    
# 締め切りの早いものから進めていく
ab.sort()
t = 0
for i in range(n):
    task = ab[i]
    t += task[1]
    if t <= task[0]:
        continue
    else:
        print('No')
        exit()
        
print('Yes')