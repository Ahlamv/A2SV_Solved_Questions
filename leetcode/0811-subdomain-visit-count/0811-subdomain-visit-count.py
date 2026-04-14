class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        arr=[]
        mp={}
        for i in range(len(cpdomains)):
            count, domain = cpdomains[i].split(" ")
            count = int(count)
            parts=domain.split(".")
            for j in range(len(parts)):
                newdomain=".".join(parts[j:]) 
                mp[newdomain]=mp.get(newdomain, 0)+ count
        for dom, count in mp.items():
        
            arr.append(str(count) + " " + dom)

        return arr