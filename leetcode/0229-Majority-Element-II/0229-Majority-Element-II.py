from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        arr=[]
        for i in range(len(nums)):
            if count[nums[i]]>len(nums)//3 and nums[i] not in arr:
                arr.append(nums[i])
        return arr