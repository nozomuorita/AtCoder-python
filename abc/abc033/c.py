"""
・プラスで区切る
・0が含まれているならそのまま
・0がないなら、そのまとまりを0とする
"""
s = input()
sp = s.split("+")

ans = 0
for i in sp:
    if "0" not in i: ans+=1

print(ans)