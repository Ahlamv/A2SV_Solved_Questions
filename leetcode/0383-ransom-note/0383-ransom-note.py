from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1=Counter(ransomNote)
        count2=Counter(magazine)
        s1=set(ransomNote)
        s2=set(magazine)
        for ch in s1:
            if ch not in s2 or count1[ch] > count2[ch]:
                return False
        return True