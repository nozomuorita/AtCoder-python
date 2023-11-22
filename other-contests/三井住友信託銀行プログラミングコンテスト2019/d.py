from collections import defaultdict
n = int(input())
s = input()
d = defaultdict(list)
for i in range(n): d[s[i]].append(i)

ans = 0
#  000-999まで試す
for i in range(1000):
    number = str(i).zfill(3)
    if (len(d[number[0]])==0) or (len(d[number[1]])==0) or (len(d[number[2]])==0): continue
    
    left=d[number[0]][0]
    right = d[number[2]][-1]
    
    for mid in d[number[1]]:
        if left<mid<right: ans+=1; break
        
print(ans)