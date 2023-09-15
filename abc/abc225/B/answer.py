n = int(input())

ab = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

for i in ab:
    if len(i)==n-1:
        print('Yes')
        exit()

print('No')