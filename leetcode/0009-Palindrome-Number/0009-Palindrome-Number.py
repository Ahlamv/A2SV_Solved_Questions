class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        news=s[::-1]
        if s==news:
            return True
        return False