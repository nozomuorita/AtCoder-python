n, m, t = map(int, input().split())
max_n = n
pre = 0
for i in range(m):
    a, b = map(int, input().split())
    n -= (a-pre)
    if n<=0:
        exit(print('No'))
    
    n += (b-a)
    n = min(max_n, n)
    pre = b

n -= (t-pre)
print('Yes') if n>0 else print('No')