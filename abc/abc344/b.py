a = []

while 1:
    tmp = int(input())
    a.append(tmp)
    
    if tmp==0: break

for i in range(len(a)-1, -1, -1):
    print(a[i])