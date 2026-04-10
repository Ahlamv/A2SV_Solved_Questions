from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)
        s=set(nums)
        for num in s:
            if count[num] == 2:
                res.append(num)
        return res



        