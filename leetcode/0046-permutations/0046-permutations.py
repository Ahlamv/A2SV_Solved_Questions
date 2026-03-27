class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(path):
            if len(path)==len(nums):
                result.append(path[:])
            for k in range(len(nums)):
                if nums[k] in path:
                    continue 
                path.append(nums[k])
                backtrack(path)
                path.pop()
        backtrack([])
        return result

        
        