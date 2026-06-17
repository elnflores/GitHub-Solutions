# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.trav_helper(root, result)
        return result
    
    def trav_helper(self, cur_node, result):
        if cur_node is None:
            return
        result.append(cur_node.val)
        self.trav_helper(cur_node.left, result)
        self.trav_helper(cur_node.right, result)
        