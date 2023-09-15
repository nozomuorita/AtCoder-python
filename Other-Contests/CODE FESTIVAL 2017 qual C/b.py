n = int(input())
a = list(map(int, input().split()))

even = 0
for i in range(n):
    if a[i]%2==0:
        even += 1
        
print(3**n - 2**even)