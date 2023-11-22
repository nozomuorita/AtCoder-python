t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, int(n**(1/3))+1):
        if n%i!=0: continue
        
        if n%(i**2)==0: print(i, n//(i**2)); break
        else: print(int((n/i)**0.5), i); break