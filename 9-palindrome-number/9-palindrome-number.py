class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = [i for i in str(x)]
        if tmp == list(reversed(tmp)): return True
        # 뒤집어도 같다면
        else: return False