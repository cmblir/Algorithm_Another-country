class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        # 기존의 nums1 리스트의 조건 m 이후는 삭제
        nums1 += nums2[:n]
        # 나머지 nums1에 nums2 조건에 맞는 리스트 합치기
        nums1.sort() # nums1 정렬