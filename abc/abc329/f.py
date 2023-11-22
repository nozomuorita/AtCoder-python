#  マージテク(集合の小さいほうを移動させる)
n, q = map(int, input().split())
d = {}
c = list(map(int, input().split()))

for i in range(len(c)):
    d[i] = set([c[i]])

for i in range(q):
    a, b = map(lambda x: x-1, map(int, input().split()))
    if len(d[a])<len(d[b]):
        d[b] |= d[a]
        d[a] = set()
    else:
        d[a] |= d[b]
        d[b] = set()
        d[b], d[a] = d[a], d[b]
    print(len(d[b]))