# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Since we must find the Layers of the binary tree : BFS

        if root is None:
            return True
        elif root.left is None:
            if root.right is None:
                return True
            elif root.right.right is None and root.right.left is None:
                return True
            else:
                return False
        elif root.right is None:
            if root.left is None:
                return True
            elif root.left.right is None and root.left.left is None:
                return True
            else:
                return False
        else:
            self.isBalanced(root.left)
            self.isBalanced(root.right)
