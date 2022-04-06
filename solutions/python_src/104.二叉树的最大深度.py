#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nodeDepth(self, depth, node):
        if node is None:
            return depth
        depth += 1
        return max(self.nodeDepth(depth, node.left), self.nodeDepth(depth, node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.nodeDepth(1, root.left), self.nodeDepth(1, root.right))
# @lc code=end
