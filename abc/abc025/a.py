s = input()
n = int(input())

W = []
for i in s:
    for j in s:
        W.append(i + j)
        
print(W[n-1])