n = int(input())
ans = ""

for i in range(10):
    s = (n//(1<<i)) % 2
    ans += str(s)

print(ans[::-1])

# n = int(input())
# ans = ""

# while n!=1:
#     ans += str(n%2)
#     n //= 2

# ans += "1"
# ans = ans[::-1]
# print(ans.zfill(10))