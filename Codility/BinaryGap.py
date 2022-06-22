def solution(N):
    # write your code in Python 3.6
    result = bin(N)[2:].strip('0').strip('1').split('1')
    return len(max(result))
