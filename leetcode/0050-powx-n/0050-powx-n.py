class Solution:
    def myPow(self, x: float, n: int) -> float:
    
        def power(n):
            if n==1:
                return x
            if n==0:
                return 1
            h=power(n//2)
            if n%2==0:
                return h*h
            else:
                return h*h*x
        if n < 0:
            return 1 / power(-n)
        return power(n)



            

        

        