n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(b) - max(a) + 1
if ans < 0:
    ans = 0
print(ans)