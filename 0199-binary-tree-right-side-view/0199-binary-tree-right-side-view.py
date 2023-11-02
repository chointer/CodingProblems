# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# N of Nodes <= 100

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            answer = [root.val]
        else:
            return []

        level_now = [root]
        level_next = []

        while level_now:
            for node in level_now:
                if node.left:
                    level_next.append(node.left)
                if node.right:
                    level_next.append(node.right)
            
            if level_next:
                answer.append(level_next[-1].val)
            
            level_now = level_next
            level_next = []
        
        return answer