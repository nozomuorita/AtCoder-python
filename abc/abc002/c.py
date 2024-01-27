p = list(map(int, input().split()))
p1 = [p[0], p[1]]
p2 = [p[2], p[3]]
p3 = [p[4], p[5]]

if p1==[0, 0]:
    ans = abs((p2[0]*p3[1]) - (p2[1]*p3[0])) / 2
elif p2==[0, 0]:
    ans = abs((p1[0]*p3[1]) - (p1[1]*p3[0])) / 2
elif p3==[0, 0]:
    ans = abs((p1[0]*p2[1]) - (p1[1]*p2[0])) / 2
else:
    ans = abs((p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0])*(p1[1]-p3[1])) / 2

print(ans)