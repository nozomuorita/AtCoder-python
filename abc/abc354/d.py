a, b, c, d = map(int, input().split())
ans = 0

x = [0, 0, 0, 0]
tmp = (c-a)//4
for i in range(4):
    x[i] += tmp
tmp = (c-a)%4
if tmp==1:
    x[(a%4)%4] += 1
elif tmp==2:
    x[(a%4)%4] += 1
    x[(a%4+1)%4] += 1
elif tmp==3:
    x[(a%4)%4] += 1
    x[(a%4+1)%4] += 1
    x[(a%4+2)%4] += 1

y = [0, 0]
tmp = (d-b)//2
for i in range(2):
    y[i] += tmp
tmp = (d-b)%2
if tmp==1:
    y[(b%2)] += 1

for i in range(4):
    for j in range(2):
        if (i==0 and j==0) or (i==1 and j==1):
            ans += x[i]*y[j]*2
        elif (i==0 and j==1) or (i==1 and j==0) or (i==2 and j==1) or (i==3 and j==0):
            ans += x[i]*y[j]

print(ans)