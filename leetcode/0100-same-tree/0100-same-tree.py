# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def issame(a,b):
            if a==None and b==None:
                return True
            if a==None and b!=None or a!=None and b==None:
                return False
            if a.val!= b.val:
                return False
            return issame(a.right,b.right) and issame(a.left,b.left)
        return issame(p,q)
            

        
        
        
        