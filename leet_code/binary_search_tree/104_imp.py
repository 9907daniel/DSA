# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive Depth Search
        if not root:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right)) 

        ###################################
        # iterative Breath Search
        if not root:
            return 0
        # when root is empty

        level = 0
        q = deque([root])
        # create queue for root

        while q:
            for i in range(len(q)):
            # range(0, 1)
                node = q.popleft()
                # q = deque([])
                # node = root still
                # first floor has been pop'd
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # continue until both left and right is None
            level += 1
        return level

        ###################################
        # Iterative Depth Search