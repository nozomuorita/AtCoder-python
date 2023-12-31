x = int(input())

beki = [1]
for i in range(2, 1001):
    v = i
    for j in range(2, 1000):
        v *= i
        if v>x: break
        beki.append(v)

beki.sort(reverse=True)
for i in range(len(beki)):
    if beki[i]<=x: exit(print(beki[i]))