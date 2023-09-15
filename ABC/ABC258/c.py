n, q = map(int, input().split())
s = list(input())

idx = 0
for i in range(q):
    j, x = map(int, input().split())
    # クエリ1：x回行うということは文字列のインデックス0の位置がずれるということ
    # 1 2の場合、末尾を先頭に持っていく操作を2回するので、結局は、末尾から2番目を先頭とみなすことと同じ
    # "abcdef"があり、「1 2」を行うと、"efabcd"となる。これは、"abcdef"のeから読み始めることと同じ
    if j == 1:
        idx = (idx-x) % n
    
    if j == 2:
        print(s[(idx+x-1)%n])