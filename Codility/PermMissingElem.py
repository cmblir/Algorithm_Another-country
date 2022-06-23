def solution(A):
    # 배열에서 중복적으로 나오지 않는 값 찾기
    if len(A) == 0: return 1
    else: return sum(range(1, len(A) + 2) - sum(A))
