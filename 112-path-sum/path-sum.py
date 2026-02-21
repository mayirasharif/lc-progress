# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # let's traverse the tree

        # given: tree root
        # expected output: true if some Sum == targetSum

        
        if not root:
            return False
        
        def findPathSum(node, calc=0):
            # base case: past leaf node (remeber, we want root-to-leaf, not root to middle tree)

            """
            if not node:
                if calc != targetSum:
                    return False
                return True
            """
            left, right = None, None

            if node.val + calc == targetSum and not node.right and not node.left:
                return True

            if node.left:
                left = findPathSum(node.left, calc + node.val)
            if node.right:
                right = findPathSum(node.right, calc + node.val)

            return left or right
        
        if not findPathSum(root):
            return False 
        else:
            return True

        # think about it...

        # start at root 5
        # 5 -> TRUE or findPathSum(8, 5)
        # 4 -> TRUE or none
        # 11 -> TRUE
        # 2 -> findPathSum(null, 22) True

        # Hmm. cant use null node to calc the final calc?
