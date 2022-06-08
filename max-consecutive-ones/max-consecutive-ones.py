class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        mx = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                # 반복문이 도는 동안 1을 만나면
                cnt += 1 # 갯수를 세준다.
                if mx < cnt: # 만약 최대 중복 갯수값보다 크다면
                    mx = cnt # 덮어주기
            else: # 만약 중복이 안된다면
                cnt = 0
        return mx