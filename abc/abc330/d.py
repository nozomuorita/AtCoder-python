"""解説放送"""
n = int(input())
s = [input() for _ in range(n)]

row, col = [], []    # 各行、各列にある〇の個数
for i in s:
    row.append(i.count("o"))
for i in range(n):
    c = 0
    for j in range(n):
        if s[j][i]=="o": c+=1
    col.append(c)

ans = 0
for i in range(n):
    for j in range(n):
        if s[i][j]=="x": continue
        circle = (row[i]-1) * (col[j]-1)
        ans += circle
        
print(ans)