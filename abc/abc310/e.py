n = int(input())
s = input()

zero, one = 0, 0
ans = 0
for i in range(n):
    if s[i]=="0":
        zero, one = 0, zero+one
        zero += 1
    else:
        zero, one = one, zero
        one += 1
    ans += one
    
print(ans)