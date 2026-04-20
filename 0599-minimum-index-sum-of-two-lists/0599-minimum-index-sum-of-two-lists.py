class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr=[]
        mp = {}
        for j, v in enumerate(list2):
            mp[v] = j
        minsum=float('inf')
        for i in range(len(list1)):
            if list1[i] in mp and mp[list1[i]]+i < minsum:
                minsum=mp[list1[i]]+i
                arr.clear()
                arr.append(list1[i])
            elif  list1[i] in mp and mp[list1[i]]+i <= minsum:
                arr.append(list1[i])
        return arr

        