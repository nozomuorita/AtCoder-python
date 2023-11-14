n = int(input())
k = int(input())

x = 1
for i in range(n):
    if x<=k: x*=2
    else: x+=k
print(x)