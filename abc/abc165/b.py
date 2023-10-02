x = int(input())
m = 100
n = 0
print(123*1.01)

while 1:
    n += 1
    m *= 101
    m //= 100
    if m>=x:
        print(n)
        exit()