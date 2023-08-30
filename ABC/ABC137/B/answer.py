k, x = map(int, input().split())

n1 = x-k+1
n2 = x+k-1

if n1<-1000000:
    n1 = -1000000
if n2>1000000:
    n2 = 1000000
    
for i in range(n1, n2+1):
    print(i, end=" ")