a, b, c = map(int, input().split())

left = 4*a*b
right = ((c-a-b)**2)
print('Yes') if (c-a-b)>0 and left<right else print('No')