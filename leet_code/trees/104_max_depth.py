from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        count = 0
        while queue:
            for a in range(len(queue)):
                # we always have to pop all in the same floor before moving on
                node = queue.popleft()
                if node.left:
                    queue.append(root.left)
                if node.right:
                    queue.append(root.right)
            count += 1
        return count