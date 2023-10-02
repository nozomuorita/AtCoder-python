n, k = map(int, input().split())

def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return str_n[::-1]

if n==0:
    print(0)
    exit()
    
for i in range(k):
    n = int(str(n), 8)
    n = base_n(n, 9)
    n = n.replace('8', '5')

print(n)