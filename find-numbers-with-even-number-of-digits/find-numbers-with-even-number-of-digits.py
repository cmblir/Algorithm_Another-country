class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                # 찾은 값이 짝수라면
                cnt += 1
        return cnt