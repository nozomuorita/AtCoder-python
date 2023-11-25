n = int(input())
s = [input() for _ in range(n)]
f = s.count("For")
print('Yes') if f>=(n//2+1) else print('No')