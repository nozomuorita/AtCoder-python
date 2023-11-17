n = int(input())
for i in range(n, 1000):
    if len(set(str(i)))==1:
        print(i)
        break