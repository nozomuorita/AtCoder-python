from math import log2
def ceil_div(x, y): return -(-x//y)
n, k = map(int, input().split())

two = 0
cnt = 0
for i in range(1, n+1):
    if i>=k: cnt+=1; continue
    tmp = ceil_div(log2(k/i)+1, 1)
    two += pow(1/2, tmp-1)

print(((1/n)*two) + (cnt*(1/n)))

# 別解
# n, k = map(int, input().split())
# ans = 0
# for i in range(1, n+1):
#     tmp = i
#     v = 1/n
#     while (tmp<k):
#         tmp *= 2
#         v /= 2
    
#     ans += v

# print(ans)