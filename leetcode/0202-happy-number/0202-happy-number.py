class Solution:
    def isHappy(self, n: int) -> bool:
        track=set()
        while n != 1:
            if n in track:
                return False
            track.add(n)
            s=str(n)
            sum=0
            for num in s:
                sum+=pow(int(num),2)
            n=sum 
        return True
        
        
        


        
        