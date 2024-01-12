n = int(input())
ans = [[0]*n for _ in range(n)]
ans[(n-1)//2][(n-1)//2] = "T"

idx = 1
for i in range(0, (n-1)//2):
    pos = [i, i]
    for d in range(4):
        if d==0:
            for j in range(n-(2*i)):
                ans[pos[0]][pos[1]] = idx
                if j!=n-(2*i)-1: pos[1] += 1
                idx += 1
                print(pos)
        elif d==1:
            pos[0] += 1
            for j in range(n-(2*i)-1):
                ans[pos[0]][pos[1]] = idx
                if j!=n-(2*i)-2: pos[0] += 1
                idx += 1
                print(pos)
        elif d==2:
            pos[1] -= 1
            for j in range(n-(2*i)-1):
                ans[pos[0]][pos[1]] = idx
                if j!=n-(2*i)-2: pos[1] -= 1
                idx += 1
                print(pos)
        else:
            pos[0] -= 1
            for j in range(n-(2*i)-2):
                ans[pos[0]][pos[1]] = idx
                if j!=n-(2*i)-3: pos[0] -= 1
                idx += 1
                print(pos)

for i in ans:
    print(*i)