m = int(input())
d = list(map(int, input().split()))

mid = (sum(d)+1)//2
s = 0
for i in range(m):
    if s+d[i]<mid: s+=d[i]
    else:
        month = i+1
        day = mid-s
        break

print(month, day)