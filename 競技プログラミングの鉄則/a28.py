n = int(input())
number = 0
for i in range(n):
    _ = list(map(str, input().split()))
    t, a = _[0], int(_[1])
    
    if t=="+":
        number += a
    elif t=="-":
        number -= a
    else:
        number *= a
    
    number %= 10000
    
    print(number)