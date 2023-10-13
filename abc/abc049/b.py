h, w = map(int, input().split())
c = [input() for _ in range(h)]

ans = []
for i in range(h):
    ans.append(c[i])
    ans.append(c[i])
    
for i in range(2*h):
    print(ans[i])