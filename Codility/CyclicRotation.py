# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    A = deque(A)
    if len(A) >= 1: # 문자열이 없는 경우 제외
        while K > 0:
            A.appendleft(A[-1])
            A.pop()
            K -= 1
    return list(A)
breakpoint()
print(solution([3,8,9,7,6],3))
