def solution(A):
    lf = 0
    rf = sum(A)
    result = None

    for i in range(1, len(A)):
        lf += A[i-1] # A[0] ... A[P-1]까지의 합
        rf -= A[i-1] # A[P] ... A[N-1]까지의 합
        tmp = abs(lf - rf) # 두 수의 차를 절대값으로 계산

        if result == None: # 반복문이 처음 돌았다면
            result = tmp
        else:
            result = min(result, tmp) # 둘 중 작은 수로 결과값을 업데이트 해준다.
    return  result
