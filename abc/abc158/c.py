a, b = map(int, input().split())

for i in range(1, 1251):
    if int(i*0.08) != a:
        continue
    if int(i*0.1) != b:
        continue
    print(i)
    exit()
    
print(-1)