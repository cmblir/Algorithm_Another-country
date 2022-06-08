class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            # 제곱수로 해당 위치 값을 변경해준다.
        return sorted(nums) # 정렬된 값을 불러온다.
            