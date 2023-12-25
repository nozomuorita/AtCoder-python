a, b, c= map(int, input().split())
k = int(input())

cnt = 0
while cnt<k and a>=b:
    b*=2
    cnt+=1

while cnt<k and b>=c:
    c*=2
    cnt+=1

print('Yes') if a<b<c else print('No')