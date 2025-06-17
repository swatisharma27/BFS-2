# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    # BFS Solution - I
    def isCousins(self, root, x: int, y: int) -> bool:
        """
        TC: O(n)
        AS: O(n)
        """
        result = []
        queue = deque()
        parentQueue = deque()

        # root is None
        if not root:
            return result
        
        queue.append(root)
        parentQueue.append(None)
        
        while queue:
            size = len(queue)
            xFound = False
            yFound = False
            xParent = ''
            yParent = ''
            
            for s in range(size):
                node = queue.popleft()
                parentNode = parentQueue.popleft()

                if x == node.val:
                    xFound = True
                    xParent = parentNode.val
                if y == node.val:
                    yFound = True
                    yParent = parentNode.val
                

                if node.left:
                    queue.append(node.left)
                    parentQueue.append(node.val)
                if node.right:
                    queue.append(node.right)
                    parentQueue.append(node.val)

            if xFound and yFound:
                return xParent != yParent
            if xFound or yFound:
                return False
            
        return False


from collections import deque
class Solution2:
    # BFS Solution - II
    def isCousins(self, root, x: int, y: int) -> bool:
            """
            TC: O(n)
            AS: O(n)
            """

            result = []
            queue = deque()

            # root is None
            if not root:
                return result
            
            queue.append(root)

            while queue:
                size = len(queue)
                xFound = False
                yFound = False
                
                for s in range(size):
                    node = queue.popleft()

                    if x == node.val:
                        xFound = True
                    if y == node.val:
                        yFound = True

                    if node.left and node.right:
                        if (x == node.left.val and y == node.right.val) or (y == node.left.val and x == node.right.val):
                            return False

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                if xFound and yFound:
                    return True
                if xFound or yFound:
                    return False
            return False
    