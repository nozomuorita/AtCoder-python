S = list(input())

# ピン1が立っているならNo
if S[0] == '1':
    print('No')
    exit()
    
# 左から順に列ごとに格納
pin = [[S[6]], [S[3]], [S[1], S[7]], [S[0], S[4]], [S[2], S[8]], [S[5]], [S[9]]]

# ピンが全て倒れているかを格納
# 倒れているなら，True, 立っているピンがあるならFalse
pin2 = []
for i in pin:
    if '1' in i:
        pin2.append(False)
    else:
        pin2.append(True)

flag = True
for i in range(5):
    for j in range(i+2, 7):
        if not(pin2[i]) and not(pin2[j]):
            tmp = pin2[i+1: j]
            if True in tmp:
                print('Yes')
                exit()
            
print('No')    