from heapq import heapify, heappop, heappush
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

heapify(a)
heapify(b)

ans = 0
buy = 0

while b:
    need = heappop(b)
    
    box = -1
    while a:
        tmp = heappop(a)
        if tmp>=need:
            box = tmp
            buy += 1
            ans += box
            break
    if box==-1:
        exit(print(-1))
    
print(ans) if buy==m else print(-1)