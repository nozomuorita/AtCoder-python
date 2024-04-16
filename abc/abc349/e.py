import sys
sys.setrecursionlimit(100000000)

def check(colors):
    if (len(set(colors))==1) and (colors[0]!=-1):
        return True
    else:
        return False

def rec(turn):
    # check row
    for i in range(3):
        r = [state[3*i+j] for j in range(3)]
        if check(r):
            ans = state[3*i]
            return ans
    # check col
    for j in range(3):
        c = [state[3*i+j] for i in range(3)]
        if check(c):
            ans = state[j]
            return ans
    # check diag1
    d1 = [state[3*i+i] for i in range(3)]
    if check(d1):
        ans = state[0]
        return ans
    # check diag2
    d2 = [state[3*i+2-i] for i in range(3)]
    if check(d2):
        ans = state[2]
        return ans
    # all painted
    if -1 not in state:
        score = [0] * 2
        for i in range(3):
            for j in range(3):
                score[state[3 * i + j]] += a[i][j]
        ans = 0 if score[0]>score[1] else 1
        return ans

    for k in range(9):
        if state[k] == -1:
            state[k] = turn
            if rec(turn ^ 1) == turn:
                state[k] = -1
                return turn
            state[k] = -1
    return turn ^ 1

a = [list(map(int, input().split())) for _ in range(3)]
state = [-1] * 9
print(["Takahashi", "Aoki"][rec(0)])