#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        number_col_value = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
                            7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
                            13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
                            19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
                            25: 'Y', 26: 'Z', 0: 'Z'}
        result = ''
        mod_result = -1
        while columnNumber > 26:
            (columnNumber, mod_result) = divmod(columnNumber, 26)
            if mod_result == 0:
                columnNumber -= 1
            result = number_col_value[mod_result] + result

        if columnNumber > 0:
            result = number_col_value[columnNumber] + result

        return result
# @lc code=end

