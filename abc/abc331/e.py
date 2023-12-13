from heapq import heapify, heappop, heappush
n, m, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b2 = sorted([(b[i], i) for i in range(m)], reverse=True)

cd = [tuple(map(lambda x: x-1, map(int, input().split()))) for _ in range(l)]
cd = set(cd)

q = []
idx = [0]*n
for i in range(n):
    q.append((-(a[i]+b2[idx[i]][0]), i))
heapify(q)

while q:
    price, i = heappop(q)
    if (i, b2[idx[i]][1]) not in cd: exit(print(-price))
    
    idx[i] += 1
    heappush(q, (-(a[i]+b2[idx[i]][0]), i))
    
# from collections import defaultdict
# n, m, l = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# dic = defaultdict(set)
# for _ in range(l):
#     c, d = map(lambda x: x-1, map(int, input().split()))
#     dic[c].add(d)

# b2 = sorted([(b[i], i) for i in range(m)], reverse=True)

# ans = -1
# for i in range(n):
#     price = a[i]
#     for j, k in b2:
#         if k not in dic[i]:
#             price += j
#             break
#     ans = max(ans, price)

# print(ans)