class Solution:
    def simplifyPath(self, path: str) -> str:
        p=path.split("/")
        stack=[]
        for dir in p:
            if dir == "..":
                if stack:
                    stack.pop()   
            else:
                if dir != "." and dir != "":
                    stack.append(dir)
        return '/' + '/'.join(stack)
                
        