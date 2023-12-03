n, q = map(int, input().split())
card = [0]*(n+1)

for i in range(q):
    z, x = map(int, input().split())
    if z==1: card[x]+=1
    elif z==2: card[x]+=2
    else:
        if card[x]>=2: print('Yes')
        else: print('No')