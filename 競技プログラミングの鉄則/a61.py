n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    
for i in range(1, n+1):
    print(f"{i}:", end=" ")
    print("{", end="")
    for j in range(len(g[i])):
        print(g[i][j], end="")
        if j!=len(g[i])-1: print(",", end=" ")
    print("}", end="\n")