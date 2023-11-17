p = list(map(int, input().split()))

ans = ''

for i in p:
     ans += chr(i+96)

print(ans)