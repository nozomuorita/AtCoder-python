import math
N = int(input())

if N <= (1e3 - 1):
    print(int(N))
elif N <= (1e4 - 1):
    N = math.floor(N /10)
    N *= 1e1
    print(int(N))
elif N <= (1e5 - 1):
    N = math.floor(N /100)
    N *= 1e2
    print(int(N))
elif N <= (1e6 - 1):
    N = math.floor(N /1000)
    N *= 1e3
    print(int(N))
elif N <= (1e7 - 1):
    N = math.floor(N /10000)
    N *= 1e4
    print(int(N))
elif N <= (1e8 - 1):
    N = math.floor(N /100000)
    N *= 1e5
    print(int(N))
elif N <= (1e9 - 1):
    N = math.floor(N /1000000)
    N *= 1e6
    print(int(N))