n = int(input())
t = input()

ans = [0, 0]
direction = 0 #0: 東、1: 南、2: 西、3: 北

for i in t:
    if i=='S':
        if direction==0:
            ans[0] += 1
        elif direction==1:
            ans[1] -= 1
        elif direction==2:
            ans[0] -= 1
        else:
            ans[1] += 1
            
    else:
        if direction != 3:
            direction += 1
        else:
            direction = 0
            
print(*ans)