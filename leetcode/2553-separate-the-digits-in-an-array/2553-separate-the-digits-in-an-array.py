class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        mp=map(str,nums)
        num="".join(mp)
        for n in num:
            arr.append(int(n))
        return arr