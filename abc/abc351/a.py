a = sum(list(map(int, input().split())))
b = sum(list(map(int, input().split())))

c = a - b + 1
print(max(c, 0))