"""
・中央値になりうるのは、真ん中にある二つの数字のどちらか
・真ん中の二つの数字が同じならどの数字を取り除いても答えは同じで、中央の値である
・二つの数字が異なる場合、取り除く数字が前半のものなら二つの数字の後ろのものが答え、そうでないなら前のものが答え
"""
n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(x)

if x_sort[n//2]==x_sort[n//2 - 1]:
    for i in range(n): print(x_sort[n//2])
    exit()

for i in range(n):
    print(x_sort[n//2]) if x[i]<=x_sort[n//2 - 1] else print(x_sort[n//2 - 1])