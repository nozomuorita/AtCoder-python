# bit全探索(全パターン列挙できるが、bit全探索で実装)
# 符号はプラスかマイナスで、全部で三つあるので、0~2**3で決定する(2なら0b010なので-+-の順として計算する)
abcd = input()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])
abcd = [a, b, c, d]

ans = []
for i in range(2**3):
    tmp = a
    ans = str(a)
    for j in range(3):
        if (i>>j)&1:
            tmp += abcd[j+1]
            ans += '+'
            ans += str(abcd[j+1])
        else:
            tmp -= abcd[j+1]
            ans += '-'
            ans += str(abcd[j+1])
    if tmp == 7:
        ans += '=7'
        print(ans)
        break