n, m = map(int, input().split())
ans = set()

for i in range(n):
    a = set(list(map(int, input().split()))[1:])
    if i==0: ans|=a
    else: ans&=a
    
print(len(ans))