n, m = map(int, input().split())
ab = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab[a].append(b)
    ab[b].append(a)

for i in range(n):
    print(len(ab[i]))