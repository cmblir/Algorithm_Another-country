import math
def solution(x, y, d):
    # x는 현재 위치, y는 목표 위치, d는 점프
    return math.ceil((y - x) / d)
