n = input()

for i in range(15):
    n2 = n[::-1]
    if n==n2: exit(print('Yes'))
    n = "0" + n

print('No')