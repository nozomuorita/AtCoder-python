# 2進数に変換したのち、文字列に変換 → replaceで2を1に変換して出力
k = int(input())

ans = str(bin(k))[2:]
ans = ans.replace('1', '2')
print(ans)