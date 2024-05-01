"""解説"""
a, b = map(int, input().split())

if a==0: a_xor=0
else:
    a_xor = 1 if ((a)//2)%2!=0 else 0
    if (a)%2!=0: a_xor^=(a-1)
if b==0: b_xor=0
else:
    b_xor = 1 if ((b+1)//2)%2!=0 else 0
    if (b+1)%2!=0: b_xor^=b

ans = a_xor ^ b_xor
print(ans)