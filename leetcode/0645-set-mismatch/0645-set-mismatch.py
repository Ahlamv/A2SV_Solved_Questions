from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        for i in range(len(nums)):
            if count[i+1] == 0:
                miss=i+1
            if count[i+1] == 2:
                twice=i+1
        return [twice, miss]


        