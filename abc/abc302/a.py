import math
A, B = map(int, input().split())
tmp = A//B
tmp2 = A % B

if tmp2 > 0:
    ans = tmp + 1
else:
    ans = tmp

#ans = math.ceil(A/B)
print(ans)