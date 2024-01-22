x, y = map(int, input().split())
group = [-1, 1, 2, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1]
print('Yes') if group[x]==group[y] else print('No')