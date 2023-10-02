def ceil_div(x, y): return -(-x//y)

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = [[] for _ in range(k)]
for i in range(n):
    c[i%k].append(a[i])

for i in range(k):
    c[i].sort()

t = -1
for j in range(ceil_div(n, k)):
    for i in range(k):
        if j < len(c[i]):
            if c[i][j]>=t:
                t = c[i][j]
            else:
                print('No')
                exit()
            
print('Yes')