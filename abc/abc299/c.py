N = int(input())
S = input()

ans_list = []
flag = True

tmp = S.split('-')
ans = len(max(tmp))

if ans == 0:
    ans = -1
    
if len(S) == ans:
    ans = -1
    

print(ans)