class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=sum(nums[k] for k in range(len(nums)) if nums[k]%2==0)
        arr=[]
        for v, i in queries:
            if nums[i] % 2 == 0:
                s-=nums[i]
            nums[i]=nums[i]+v
            if nums[i] % 2 == 0:
                s+=nums[i]  
            arr.append(s)
        return arr


        