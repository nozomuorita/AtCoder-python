k = int(input())

mod_k = []
n = 0
while len(mod_k)<k:
    n = 10*n + 7
    n %= k
    mod_k.append(n)
    if n==0:
        print(len(mod_k))
        exit()
        
print(-1)