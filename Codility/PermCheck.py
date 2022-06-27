def solution(A):
    A.sort()
    tmp = 0
    for i in A:
        if tmp + 1 != i:
            return 0
        tmp = i
    return 1
