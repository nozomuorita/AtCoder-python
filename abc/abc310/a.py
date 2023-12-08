n, p, q = map(int, input().split())
d = list(map(int, input().split()))

print(p) if p<=(q+min(d)) else print(q+min(d))
