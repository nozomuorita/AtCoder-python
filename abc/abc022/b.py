n = int(input())
a = [int(input()) for _ in range(n)]

flower = set()
ans = 0

for i in a:
    if i in flower: ans+=1
    flower.add(i)
    
print(ans)