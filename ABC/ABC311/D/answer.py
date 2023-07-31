# AC
from collections import deque
n, m = map(int, input().split())
s = [input() for _ in range(n)]

visited = [[False]*m for _ in range(n)] # 訪問済みかどうか
visited[1][1] = True # 初期位置は訪問済み
q = deque() # これから探索するマス(岩にぶつかって止まったマス→方向転換の起点)
q.append((1, 1)) # 初期位置

ap = set() # キューに突っ込んだ座標を格納(すでに探索したマスをもう一度見ないようにする)
ap.add((1, 1)) # 初期位置はキューに追加済み

# 探索するマスがなくなるまで
while q:
    x, y = q.popleft() # キューから探索するマスを取得
    
    # 変化量(上下左右)ごとにさらに探索し、次の方向転換の起点を探す
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        i, j = x, y
        flag = True # 岩マスにぶつかるまで進み続ける
        while flag:
            # 変化量分進める
            i += dx
            j += dy
        
            # もし、氷マスなら訪問済みに追加
            if s[i][j]=='.':
                visited[i][j] = True
                
            # 岩マスならば、flagをFalseとしてその一つ前のマスを次の探索マスとする(岩にぶつかった一つ前のマスが方向転換マスとなるため)
            else:
                flag = False
                # もし、まだキューに追加していない(探索していない)マスならば、追加、そうでないならば追加しない
                if (i-dx, j-dy) not in ap:
                    ap.add((i-dx, j-dy))
                    q.append((i-dx, j-dy)) # 岩にぶつかったらその一つ前(氷マスであるはず)を次に見るマスとしてキューに追加
                
ans = 0
for i in range(n):
    ans += visited[i].count(True)
    
print(ans)