# N(node) <= 1e4
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 리스트로 flatten -> sort -> 두 값 차이 계산, min 기록 => ~O(N + NlogN) ?
# 각 node에서 상위에서 가장 가까운 숫자와 차이 계산 => ~O(2N?)
# 재귀 없이 구현해보기;  왼쪽부터 탐색, 모두 탐색하면 상위로 돌아가기, stack

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        node_stack = [(root, None, None)]       # (Node, high_left, high_right)
        answer = 1e6
        
        while node_stack:
            node, high_left, high_right = node_stack.pop()
            
            if high_left is not None:
                answer = min(answer, node.val - high_left)
            if high_right is not None:
                answer = min(answer, high_right - node.val)

            if node.left:
                node_stack.append((node.left, high_left, node.val))
            if node.right:
                node_stack.append((node.right, node.val, high_right))

        return answer