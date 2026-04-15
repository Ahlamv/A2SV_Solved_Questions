
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        while i < n:
            content = nums[i]-1
            if nums[i]!=nums[content]:
                nums[i], nums[content] = nums[content] , nums[i]
            else:
                i+=1
        res=[]
        for j in range(n):
            if nums[j] != j + 1:
                res.append(nums[j])
        return res




        