h = int(input())

n = 0
while h!=1:
    n += 1
    h //= 2
    
ans = ((2**n)-1//(2-1)) + (2**n)
print(ans)