n = int(input())
a = list(map(int, input().split()))

four = [0]*3
for i in a:
    if i%4==0: four[2]+=1
    elif i%2==0: four[1]+=1
    else: four[0]+=1

if four[2]+1==four[0] and four[0]+four[2]==n: exit(print("Yes"))
if four[2]>=four[0]: exit(print("Yes"))

print("No")
