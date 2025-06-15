# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def inorder(root, lst):
            if root is None:
                return 
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
        lst=[]
        inorder(root, lst)
        return lst
        
        
