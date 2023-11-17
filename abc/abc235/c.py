from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(list)

# キー：数列aの値(a_i)
# 値：キーの数字が登場する要素番号
for i in range(n):
    d[a[i]].append(i+1)

for i in range(q):
    x, k = map(int, input().split())

    if len(d[x])<k:
        print(-1)
    else:
        print(d[x][k-1])