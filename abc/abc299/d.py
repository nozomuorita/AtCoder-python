"""
・二分探索的な考え方
"""
n = int(input())
left = 0
right = n-1
lst = [-1]*n
lst[0], lst[-1] = 0, 1

for _ in range(20):
    mid = (left+right)//2
    
    print('? ' + str(mid+1))
    o = int(input())
    
    lst[mid] = o
    if lst[mid]!=lst[mid+1] and lst[mid+1]!=-1:
        exit(print('! '+str(mid+1)))
    
    if o==0: left=mid
    else: right=mid