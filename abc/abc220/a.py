A, B, C = map(int, input().split())

ac = A // C
bc = B // C

for i in range(ac, bc+1):
    if A <= i*C <= B:
        print(i*C)
        exit()
        
print(-1)