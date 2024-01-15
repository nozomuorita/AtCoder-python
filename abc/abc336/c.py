n = int(input())
n -= 1

ans = ""
even = [0, 2, 4, 6, 8]

ans += str(even[(n%5)])
n = n//5
while n>=5:
    ans += str(even[n%5])
    n//=5

if n!=0: ans += str(even[n])

print(ans[::-1])