from collections import defaultdict

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
s = input()

# 衝突する条件は以下の２つ
# 1. y軸方向について同じ高さにいる
# 2. 同じ高さにいる二点についてx座標が小さいほうは右、大きいほうは左へ移動するペアが存在

d_right = defaultdict(list) # 右へ移動する点を管理(キー：y座標, 値：x座標(リスト))
d_left = defaultdict(list) # 左へ移動する点を管理(キー：y座標, 値：x座標(リスト))

# 各点を辞書に追加
for i in range(n):
    x = xy[i][0]
    y = xy[i][1]
    LR = s[i]

    # 人iがR(右)へ行くなら、d_rightへ追加
    if LR == 'R':
        d_right[y].append(x)
    # 人iがL(左)へ行くなら、d_leftへ追加
    else:
        d_left[y].append(x)

# すべてのy座標を重複なしで取得(すべてのyについて条件2を調べるため)
Y = list(set([i[1] for i in xy]))
for y in Y:
    # もし、「(y座標)=yであり、かつ、右へ移動するものがない」か「(y座標)=yであり、かつ、左へ移動するものがない」ならば、そのy座標では衝突しないのでcontinue
    if (len(d_right[y])==0) or (len(d_left[y])==0):
        continue

    # 右に行く点のうち、x座標が最小のものと、左に行く点のうち、x座標が最大のものを比較
    # 以下を満たす場合、衝突するといえる
    if min(d_right[y]) < max(d_left[y]):
        print('Yes')
        exit()

print('No')