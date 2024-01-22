n = int(input())

for i in range(30):
    for j in range(30):
        if 4*i+7*j==n: exit(print('Yes'))

print('No')