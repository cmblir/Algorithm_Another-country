def solution(N):
    # 스쿠터는 중간에 버리면 더 이상 탈 수가 없다.
    N = N.replace("A",'20 ').replace("S",'30 ')
    walk = [int(i) for i in N.split()]
    # 도보로만 걷는 경우를 만든다.
    result = [sum(walk)]
    for i in range(len(walk)): # 스쿠터로 가는 경우를 매 순간마다 추가해준다.
        if walk[i] == 20: # 아스팔트인 경우
            walk[i] = 5
            result.append(sum(walk))
        elif walk[i] == 30: # 모래인 경우
            walk[i] = 40
            result.append(sum(walk))
    return min(result) # 모든 결과값중 최소값만 출력한다.
