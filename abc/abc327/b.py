b = int(input())

for i in range(1, 10**7):
    if pow(i, i)==b:
        exit(print(i))

print(-1)