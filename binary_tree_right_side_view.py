# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BFSSolution:
    def rightSideView(self, root) -> list[int]:
        """
        TC: O(n)
        AS: o(n)
        """

        result = []
        queue = deque()

        if not root:
            return []

        queue.append(root)

        while queue:

            size = len(queue)

            for s in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
                if s == size - 1:
                    result.append(node.val)
        
        return result


class DFSSolution:
    def rightSideView(self, root) -> list[int]:
        """
        TC: O(n); n: number of nodes
        AS: O(h); h: height of the tree
        """
        result = []

        def dfs(root, level):

            # base logic
            if not root:
                return 

            # logic
            if level == len(result):
                result.append(root.val)
            else:
                result[level] = root.val

            level += 1

            dfs(root.left, level)
            dfs(root.right, level)

        dfs(root, 0)
        return result
