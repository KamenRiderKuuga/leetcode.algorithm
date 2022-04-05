#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def good_enough(self, root, x):
        return abs(root * root - x) < 0.01

    def mySqrt(self, x: int) -> int:
        root = 1
        while(self.good_enough(root, x) == False):
            root = (root + x / root) / 2
        return int(root)
# @lc code=end
