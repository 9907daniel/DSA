# Max length of binary tree is worst case
# --> BigO(n)



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive Depth Search
        left_count = 0
        left_root = root
        while left_root is not None:
            left_count += 1
            left_root = left_root.left

        right_count = 0
        right_root = root
        while right_root is not None:
            right_count += 1
            right_root = right_root.right

        return max(right_count, left_count)

        
        
        