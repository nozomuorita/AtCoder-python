n = int(input())
a = []
for i in range(n):
    a_ = input()
    a.append(a_)
    
ans = []

for i in range(n):
    if i==0:
        tmp = a[i][:-1]
        tmp = a[i+1][0] + tmp
        ans.append(tmp)
    elif i==n-1:
        tmp = a[i][1:]
        tmp += a[i-1][-1]
        ans.append(tmp)
    else:
        tmp = a[i+1][0]
        for k in range(1, n-1):
            tmp += a[i][k]
        tmp += a[i-1][-1]
        ans.append(tmp)
        
for i in range(n):
    print(ans[i])