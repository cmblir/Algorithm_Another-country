class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cnt = 0
        for i in operations:
            if "+" in i: cnt += 1
            elif "-" in i: cnt -= 1
        return cnt