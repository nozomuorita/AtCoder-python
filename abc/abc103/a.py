a = list(map(int, input().split()))

a.sort(reverse=True)
print(abs(a[1]-a[0]) + abs(a[2]-a[1]))