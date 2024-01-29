"""愚直にやってもいける"""
n, k = map(int, input().split())
d = list(map(str, input().split()))
n = str(n)

while 1:
    ok = True
    for i in n:
        if i in d:
            ok = False
            break
    if ok: exit(print(n))
    
    n = str(int(n)+1)