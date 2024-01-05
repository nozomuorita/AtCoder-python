n, q = map(int, input().split())
a = list(map(int, input().split()))
a_cum = [0]
for i in range(n):
    a_cum.append(a_cum[-1]+a[i])

for _ in range(q):
    l, r = map(int, input().split())
    print(a_cum[r]-a_cum[l-1])