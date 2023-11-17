abc = input()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

ans = 0
ans += 100*a + 10*b + c
ans += 100*b + 10*c + a
ans += 100*c + 10*a + b
print(ans)