from collections import Counter 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set(nums)
        count=Counter(nums)
        for num in s:
            if count[num] > 1:
                return num
