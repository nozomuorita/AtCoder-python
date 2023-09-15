from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

n_list = set()
for i in range(1, n+1):
    n_list.add(i)

d = defaultdict(int)

for i in a:
    d[i] += 1
    if d[i]==4:
        n_list.remove(i)

print(*n_list)