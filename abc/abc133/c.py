l, r = map(int, input().split())

ans = 2020

for i in range(l, r):
    for j in range(i+1, r+1):
        tmp = ((i%2019) * (j%2019)) % 2019  # でかい値は、逐次modをとる！！
        if tmp < ans:
            ans = tmp
        if ans == 0:  # 理論上の最小値は0なので、0になったら終了する
            print(0)
            exit()
            
print(ans)