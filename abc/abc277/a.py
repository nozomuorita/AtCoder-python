N, X = map(int, input().split())
P = list(map(int, input().split()))

for i in range(len(P)):
    if P[i] == X:
        ans = i+1
        break
        
print(ans)