class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right=max(weights), sum(weights)
        while left < right:
            mid= (left + right)//2
            if  self.check(weights, mid) <= days:
                right=mid
            else:
                left=mid+1
        return right

    def check(self, weights, mid):
        day=1
        sm=0
        for s in weights:
            if sm+s > mid:
                sm=0
                day+=1 
            sm+=s
        return day

        