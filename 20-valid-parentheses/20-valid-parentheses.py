class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # 스택으로 해결
        tmp = {")":"(",
        "]":"[",
        "}":"{"}
        # 괄호 열고 닫고 정보 저장
        for i in s:
            if i in tmp.values(): # 만약 괄호가 열리는 경우
                stack.append(i) 
            else:
                if stack and tmp[i] == stack[-1]:
                    # 현재 스택이 존재하고 쌓여있으면서 괄호가 닫히는 경우
                    stack.pop()
                else:
                    # 닫을 괄호가 스택에 없거나 열린 괄호랑 다를 경우
                    return False
        
        if stack: return False
        else: return True