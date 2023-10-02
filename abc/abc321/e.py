t = int(input())
f = []
for i in range(t):
    n, x, k = map(int, input().split())
    
    ans = 0
    tmp = 0
    if k==0:
        print(1)
        f.append(1)
        continue
    for j in range(70):
        tmp += 2**j
        if tmp >= x:
            depth = j   # xの深さ
            break
    #print(depth)
    if x <= ((2**(depth+1))-1)-(2**depth // 2):
        if depth-k>0:
            ans += (2**(depth-k)) // 2
        elif depth-k==0:
            ans += 1
        
        if 2**(depth+k) <= n:
            a = 2**(depth+k+1) - 1 - (2**(depth+k)//2)
            if a <= n:
                ans += 2**(depth+k)//2
            else:
                ans += (2**(depth+k)//2)-(a - n)
            
        if k-depth>=0:
            b = 2**(k-depth+1)-1 - (2*(k-depth)//2) + 1
            c = 2**(k-depth+1)-1
            if c <= n:
                ans += (2**(k-depth))//2
            elif b <= n:
                ans += n - b
        f.append(ans)
        print(ans)
    else:
        if depth-k>0:
            ans += (2**(depth-k)) // 2
        elif depth-k==0:
            ans += 1
        if 2**(depth+k)+((2**(depth+k))//2) <= n:
            a = 2**(depth+k+1) - 1 - (2**(depth+k)//2) + 1
            if (2**(depth+k+1)-1) <= n:
                ans += 2**(depth+k)//2
            else:
                ans += (2**(depth+k+1)-1)-n
            
        if k-depth>0:
            b = 2**(k-depth)
            c = 2**(k-depth) + (2**(k-depth)//2) - 1
            if b <= n:
                if c <= n:
                    ans += 2**(k-depth)//2
                else:
                    ans += (2**(k-depth)//2) - (c - n)
            
            # b = 2**(k-depth+1)-1 - (2*(k-depth)//2) + 1
            # c = 2**(k-depth+1)-1
            # if c <= n:
            #     ans += (2**(k-depth))//2
            # elif b <= n:
            #     ans += n - b
                
        f.append(ans)
        print(ans)
        
print(*f)