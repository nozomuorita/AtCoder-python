n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]

l_sum, r_sum = 0, 0
for i in range(n):
    l_sum += lr[i][0]
    r_sum += lr[i][1]

if l_sum>0 or r_sum<0: exit(print('No'))

x = [i[0] for i in lr]
x_sum = sum(x)

for i in range(n):
    x[i] += min(abs(x_sum), lr[i][1]-lr[i][0])
    x_sum += min(abs(x_sum), lr[i][1]-lr[i][0])

print('Yes')
print(*x)