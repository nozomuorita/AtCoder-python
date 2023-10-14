A, B, K = map(int, input().split())
num = A
ans = 0

while (num<B):
  num *= K
  ans += 1
  
print(ans)