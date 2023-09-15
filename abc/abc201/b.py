n = int(input())
st = []
for i in range(n):
    s, t = map(str, input().split())
    tmp = [int(t), s]
    st.append(tmp)
    
st.sort()
print(st[-2][1])
    