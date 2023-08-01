s1 = input()
s2 = input()

n = s1.count('#') + s2.count('#')

# 黒が2つの場合
if n==2:
    if (s1[0]=='#' and s2[1]=='#') or (s1[1]=='#' and s2[0]=='#'):
        print('No')
    else:
        print('Yes')

else:
    print('Yes')