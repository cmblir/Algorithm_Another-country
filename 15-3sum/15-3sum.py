class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3중 반복문을 사용하되, 처음 i값이 j, k 반복문과 달라야하며
        # 3값을 더한 값이 0이여야 한다.
        result = []
        nums.sort()
        # 이분탐색 알고리즘 사용
        n = len(nums)
        for i in range(n - 2):
            lf = i + 1 # 좌
            rf = n - 1 # 우
            
            if i > 0 and nums[i] == nums[i - 1]: continue
            while lf < rf:
                tmp = nums[i] + nums[lf] + nums[rf]
                # 계산해야 할 값
                if tmp > 0: # 0보다 큼 -> 큰수를 당긴다.
                    rf -= 1
                elif tmp < 0: # 0보다 작음 -> 작은수를 당긴다.
                    lf += 1
                else:
                    idx = [nums[i], nums[lf], nums[rf]]
                    if idx not in result: result.append(idx)
                        # 중복되지 않은 경우(이미 리스트에 없는 경우에만 삽입)
                    lf += 1 # 좌에서 한칸 당기고
                    rf -= 1 # 우에서 한칸 당기고
        return result
            