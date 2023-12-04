n = int(input())
a = list(map(int, input().split()))

parent = [0]*(2*n+1)
for i in range(n):
    tp = parent[a[i]-1]
    parent[2*(i+1)-1] = tp + 1
    parent[2*(i+1)] = tp + 1

for i in parent: print(i)