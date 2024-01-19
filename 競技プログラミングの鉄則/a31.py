"""包除原理"""
n = int(input())

three = n//3
five = n//5
gcd = n//15

print(three+five-gcd)