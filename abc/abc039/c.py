s = input()
kenban = "WBWBWWBWBWBW" * 5
white = [i for i in range(len(kenban)) if kenban[i]=="W"]
ans = "DoReMiFaSoLaSi_"

for i in range(7):
    idx = 2*i
    j = white[i]
    if kenban[j:j+20]==s:
        exit(print(ans[idx:idx+2]))