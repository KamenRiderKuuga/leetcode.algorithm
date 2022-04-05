#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printLeftAndRight(self, result, level, node):
        if node.left is None and node.right is None:
            return
        if len(result) - 1 < level:
            result.append([])
        if node.left is not None:
            result[level].append(node.left.val)
            self.printLeftAndRight(result, level + 1, node.left)
        if node.right is not None:
            result[level].append(node.right.val)
            self.printLeftAndRight(result, level + 1, node.right)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result = [[root.val]]
        self.printLeftAndRight(result, 1, root)
        return result
# @lc code=end
