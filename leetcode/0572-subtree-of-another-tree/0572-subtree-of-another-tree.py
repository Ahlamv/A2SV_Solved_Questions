# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isidentical(r,s):
            if r==None and s==None:
                return True
            if r==None and s!=None or r!=None and s==None:
                return False
            if r.val != s.val:
                return False
            return isidentical(r.right,s.right) and isidentical(r.left,s.left)  
 
        if not root:
            return False
        if isidentical(root,subRoot):
            return True
        
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)