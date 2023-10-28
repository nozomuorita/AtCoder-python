n = int(input())
mod = 10007

a = [0, 0, 1]

if n<=3: exit(print(a[n-1]))

for i in range(n-3):
    t = a[-1]+a[-2]+a[-3]
    a.append(t%mod)
    
print(a[-1])