def solution(X, A):
    dp = [False] * X
    tmp = 0
    for i, j in enumerate(A):
        if dp[j - 1] == False:
            dp[j - 1] = True
            tmp += 1
            if tmp == X:
                return i
    return -1
