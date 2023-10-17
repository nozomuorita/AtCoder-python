n = int(input())
a = list(map(int, input().split()))

mx1 = max(a[:((2**n)//2)])
mx2 = max(a[((2**n)//2):])
print(a.index(min(mx1, mx2))+1)