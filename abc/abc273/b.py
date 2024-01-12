x, k = map(int, input().split())
for i in range(k):
    r = (x//10**i) % 10
    if r>=5:
        x = ((x//10**(i+1))+1) * (10**(i+1))
    else:
        x = ((x//10**(i+1))) * (10**(i+1))
        
print(x)