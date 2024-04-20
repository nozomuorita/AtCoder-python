n, q = map(int, input().split())
t = list(map(int, input().split()))
teeth = [True]*n

for i in range(q):
    tmp = t[i]-1
    if teeth[tmp]:
        teeth[tmp] = False
    else:
        teeth[tmp] = True

print(teeth.count(True))