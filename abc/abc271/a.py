N = int(input())

# 10進数から16進数への変換
# Nを16で割っていき，商が0になるまで繰り返す
# 商の0とそれまでのあまりを逆から読むと答えになる

# N=0の場合は，00となる(例外処理とする)
if N==0:
    print('00')
    exit()

shou = N  # 16で割った余り
r_list = []  # 余りを入れるリスト
chr_list = ['A', 'B', 'C', 'D', 'E', 'F']  # 10~15に対応するもの

while (shou != 0):
    r = shou % 16
    if r < 10:
        r_list.append(str(r))
    else:
        tmp = r - 10
        r_list.append(chr_list[tmp])
        
    shou = shou //16
    
ans = ''.join(reversed(r_list))
if len(ans) < 2:
    ans = '0' + ans

print(ans)