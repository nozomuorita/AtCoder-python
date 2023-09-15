n, m = map(int, input().split())
l = list(map(int, input().split()))

# 横幅の文字数を二分探索で探す
left = max(l) - 1      #  ありうる最小の横幅は一つの単語だけ並ぶ場合なので、一番文字数の長い単語となる
right = sum(l) + n - 1   #  ありうる最大の横幅は、すべての単語が一行に並ぶ場合(最後の単語は空白がいらないので-1とする)

while abs(left-right)>1:
    # 幅がmid文字のとき
    mid = (left + right) // 2
    c = 0                       #  総文字数
    row = 1                     #  総行数
    
    for i in range(n):
        c += l[i] + 1
        # 横幅がmidを超えるなら、そのひとつ前までで改行する
        # 今見ているものは、次の行に書かれるので、次の行に足す
        if c-1 > mid:
            row += 1
            c = l[i] + 1
            
    if row > m:
        left = mid
    else:
        right = mid
        
print(right)