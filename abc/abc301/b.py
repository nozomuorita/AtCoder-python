from collections import deque
N = int(input())
A = list(map(int, input().split()))
ans = deque()
ans.append(A[0])

for i in range(1, len(A)):
    ab = abs(ans[-1]-A[i])
    if ab==1:
        ans.append(A[i])
        
    else:
        if ans[-1] > A[i]:
            tmp = ans[-1]-1
            for j in range(ab):
                ans.append(tmp)
                tmp -= 1
        else:
            tmp = ans[-1] + 1
            for j in range(ab):
                ans.append(tmp)
                tmp += 1
                
print(*ans)