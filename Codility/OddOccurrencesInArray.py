def solution(A):
    if len(A) == 1: return A[0] # 리스트내 값이 1개밖에 없는 경우
    A.sort()
    for i in range(0, len(A), 2): # 0부터 짝수임을 확인하기 위해 2칸씩 이동한다.
        if i + 1 == len(A): return A[i] # 만약 해당 위치 + 1이 마지막인 경우
        if A[i] != A[i + 1]: return A[i] # 해당 위치와 다음 위치값이 다른 경우 
        # 짝수로 이동하는데 다음 값이 만약 다르다면 해당 값은 짝이 없는 것이 된다.
