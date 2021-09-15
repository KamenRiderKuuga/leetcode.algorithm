#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        strValue = ''
        if x < 0:
            negative = True
            strValue = str(x)[:0:-1]
        else:
            strValue = str(x)[::-1]

        if negative:
            strValue = '-' + strValue

        result = int(strValue)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
# @lc code=end
