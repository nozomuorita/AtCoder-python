"""double sweep method"""
import sys
n = int(input())

v1, mx = -1, -1
for i in range(2, n+1):
    print("?", 1, i)
    sys.stdout.flush()
    dist = int(input())
    
    if dist>mx:
        mx = dist
        v1 = i

ans = -1
for i in range(1, n+1):
    if i==v1: continue
    print("?", v1, i)
    sys.stdout.flush()
    dist = int(input())
    
    if dist>ans: ans=dist
    
print("!", ans)