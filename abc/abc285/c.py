"""
・ABCDEという文字列の場合、右から順にi=0, 1, 2, 3, 4として、(26**i) * (アルファベットの順番)となる
・これを足していく
・一番右のEは26**0 * 5 = 5番目である
・Dは26**1 * 4
"""
s = list(input())
s = list(reversed(s))

ans = 0
for i in range(len(s)):
    idx = ord(s[i]) - ord("A") + 1
    ans += (26**i) * idx

print(ans)