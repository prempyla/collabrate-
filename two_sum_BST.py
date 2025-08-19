'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
'''    
def inorder(root, arr):
    if root is None:
        return 
    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)

def findTarget(root, k):
    lst = []
    inorder(root, lst)
    left,right = 0, len(lst) - 1
    while left < right:
        mid = lst[left] + lst[right]
 
        if mid == k:
            return True
        
        elif mid < k:
            left += 1

        else:
            right -= 1
    return False
