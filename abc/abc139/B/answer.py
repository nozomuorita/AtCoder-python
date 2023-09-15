A, B = map(int, input().split())
dA = A - 1
ans = 1

while (A < B):
  ans += 1
  A += dA
  
if B == 1:
  ans = 0
  
print(ans)