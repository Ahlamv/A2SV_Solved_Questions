from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s=0
        charc=Counter(chars)
        for word in words:
            count=Counter(word)
            n=True
            for ch in word:
                if ch not in chars or count[ch]>charc[ch]:
                    n=False
            if n:
                s=len(word)+s
        return s



        