a, b, c = map(int, input().split())
ans = 0

ans += c // min(a,b)
print(ans)