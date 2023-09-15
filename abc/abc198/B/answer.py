n = input()

if n == n[: : -1]:
    print('Yes')
    exit()

for i in range(9):
    n = '0' + n
    n_reverse = n[: : -1]

    if n == n_reverse:
        print('Yes')
        exit()

print('No')