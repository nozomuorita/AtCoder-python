from collections import defaultdict
Q = int(input())
d = defaultdict(int)
for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0]=="1":
        name, score = query[1], int(query[2])
        d[name] = score
    else:
        name = query[1]
        print(d[name])