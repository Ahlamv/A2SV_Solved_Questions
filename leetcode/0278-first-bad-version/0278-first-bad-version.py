# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res=[]
        left=0
        right=n
        while left< right:
            if n==1:
                return 1
            mid=(left+right)//2
            if isBadVersion(mid) == True:
                right=mid
            elif isBadVersion(mid) == False:
                left=mid+1
        return right
                        
            

        
        