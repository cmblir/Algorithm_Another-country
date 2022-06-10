class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + (n *(nums[nums[i]]%n))
            # 현재 위치에 현재 위치값 + 전체 길이 * 현재 위치값이 있는 위치값을 전체 길이로 나눈 값
        for i in range(n):
            nums[i] = int(nums[i]/n)
            # 위에서 전체 길이로 곱하였기때문에 다시 전체 길이로 나누어준다.
        return nums