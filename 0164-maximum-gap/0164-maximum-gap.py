class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        l=0
        r=1
        nums.sort()
        if len(nums) < 2 :
            return 0
        else:
            m=0
            while r < len(nums):
                m=max(m, abs(nums[l]-nums[r]))
                l+=1
                r+=1
        return m
            

        