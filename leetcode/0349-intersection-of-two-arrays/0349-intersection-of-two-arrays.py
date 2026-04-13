class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        arr=[]
        nums=list(s1)
        for i in range(len(nums)):
            if nums[i] in s2:
                arr.append(nums[i])
        return arr
