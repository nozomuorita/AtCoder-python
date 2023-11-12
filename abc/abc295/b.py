R, C = map(int, input().split())
B = []
for i in range(R):
    tmp = list(input())
    B.append(tmp)
    
# 爆弾のある場所を探す
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num_dict = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]} # 数字が書かれた場所を管理
for i in range(R):
    for j in range(C):
        if B[i][j] in num:
            num_dict[int(B[i][j])].append([i, j])
            
# 数字が書かれた場所に対して一つずつ爆発させる
for key in num_dict.keys():
    for n in num_dict[key]:
        r = n[0]
        c = n[1]
        for i in range(R):
            for j in range(C):
                dist = abs(r-i) + abs(c-j)
                if dist <= key:
                    B[i][j] = '.'
                
for row in range(R):
    print(''.join(B[row]))