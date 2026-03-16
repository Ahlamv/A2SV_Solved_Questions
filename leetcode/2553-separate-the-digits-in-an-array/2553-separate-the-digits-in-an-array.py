class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr=[]
        num="".join(map(str, nums))
        for n in num:
            arr.append(int(n))
        return arr