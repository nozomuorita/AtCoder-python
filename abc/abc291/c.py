n = int(input())
s = input()

z = set([(0, 0)])
pos = [0, 0]
for i in s:
    if i=="R": pos[0]+=1
    elif i=="L": pos[0]-=1
    elif i=="U": pos[1]+=1
    else: pos[1]-=1
    
    if tuple(pos) in z: exit(print('Yes'))
    z.add(tuple(pos))

print('No')