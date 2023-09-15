N = int(input())
A = list(map(int, input().split()))

# 偶数(奇数)が2つ以上存在するか
even_num = 0
odd_num = 0
flag = False
for i in A:
    if i % 2 ==0:
        even_num += 1
    else:
        odd_num += 1
    if (even_num > 1) or (odd_num > 1):
        flag = not(flag)
        break
        
if not(flag):
    print(-1)
    exit()
    
else:
    even_list = []
    odd_list = []
    for i in A:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
            
    num1, num2 = -1, -1
    # odd
    odd_list.sort()
    if len(odd_list)>1:
        num1 = odd_list[-1] + odd_list[-2]
    # even
    even_list.sort()
    if len(even_list)>1:
        num2 = even_list[-1] + even_list[-2]
    
    print(max(num1, num2))