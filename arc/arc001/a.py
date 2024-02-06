n = int(input())
s = input()

mx, mn = -1, 1000
for i in range(1, 5):
    score = s.count(str(i))
    mx = max(mx, score)
    mn = min(mn, score)

print(mx, mn)