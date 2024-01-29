from collections import deque
sa = deque(list(input()))
sb = deque(list(input()))
sc = deque(list(input()))

turn = "a"
while 1:
    if turn=="a":
        if len(sa)==0: exit(print("A"))
        turn = sa.popleft()
    elif turn=="b":
        if len(sb)==0: exit(print("B"))
        turn = sb.popleft()
    else:
        if len(sc)==0: exit(print("C"))
        turn = sc.popleft()
