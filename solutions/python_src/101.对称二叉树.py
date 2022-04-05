#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def childrenIsSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if (left is None and right is not None) or (right is None and left is not None):
            return False
        if left.val == right.val:
            return self.childrenIsSymmetric(left.left, right.right) and self.childrenIsSymmetric(left.right, right.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.childrenIsSymmetric(root.left, root.right)
# @lc code=end
