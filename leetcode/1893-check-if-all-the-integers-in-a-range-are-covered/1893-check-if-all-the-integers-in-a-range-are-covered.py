class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for ch in range(left, right+1):
            for num in ranges:
                if ch <= num[1] and ch >= num[0]:
                    break
            else:
                return False
        return True
            