n = int(input())
if n==0: exit(print(0))

ans = ""
while n!=0:
    ans += str(n % 2)
    n -= n%2
    n //= -2

print(ans[::-1])