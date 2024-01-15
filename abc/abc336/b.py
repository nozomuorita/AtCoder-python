n = int(input())
b = bin(n)[2:][::-1]

ans = 0
for i in range(len(b)):
    if b[i]=="0": ans += 1
    else: break

print(ans)