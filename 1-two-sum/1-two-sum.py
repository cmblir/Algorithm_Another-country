class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            # nums 리스트 0부터 비교
            for j in range(i+1, len(nums)):
                # 이중반복문으로 해당 위치와 다음 위치를 동시에 비교
                if nums[i] + nums[j] == target:
                    # 만약 2개값을 더한게 타겟값과 같다면
                    result.append(i)
                    result.append(j)
        return result