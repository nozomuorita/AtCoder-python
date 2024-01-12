dist = [3, 1, 4, 1, 5, 9]
dist_cum = [0]
for i in dist:
    dist_cum.append(dist_cum[-1]+i)

p, q = map(str, input().split())
p = ord(p) - ord("A")
q = ord(q) - ord("A")

print(dist_cum[max(p, q)] - dist_cum[min(p, q)])