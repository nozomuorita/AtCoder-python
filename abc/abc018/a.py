a = int(input())
b = int(input())
c = int(input())

list_ = [a, b, c]
list_.sort(reverse=True)
ans = [0, 0, 0]

for i in range(len(list_)):
    if list_[i]==a:
        ans[0] = i+1
    elif list_[i]==b:
        ans[1] = i+1
    else:
        ans[2] = i+1
        
for i in ans:
    print(i)