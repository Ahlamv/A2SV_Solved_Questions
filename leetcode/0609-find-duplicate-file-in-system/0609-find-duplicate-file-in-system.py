class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        result=[]
        for path in paths:
            path=path.split(" ")
            folder=path[0]
            for s in path[1:]:
                s=s.split("(")
                name=s[0]
                content=s[1]
                content = content[:-1]
                mp[content].append((folder,name))
        for ct, v in mp.items():
            if len(v)>1:
                res=[]
                for pre, post in v:
                    res.append(pre+"/"+post)
                result.append(res)
        return result


            

        