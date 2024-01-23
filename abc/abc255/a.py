r, c = map(lambda x:x-1, map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(2)]
print(a[r][c])