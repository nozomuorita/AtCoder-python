#  ipad メモ
def ceil_div(x, y): return -(-x//y)
n = int(input())
T, A = map(int, input().split())
for i in range(n-1):
    t, a = map(int, input().split())

    mx = max(ceil_div(T, t), ceil_div(A, a))
    
    T = t * mx
    A = a * mx

print(T + A)