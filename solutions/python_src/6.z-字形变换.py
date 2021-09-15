#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result_rows = []
        s_len = len(s)
        index = 0
        group_count = list(range(0, numRows + (numRows - 2)))
        row_count = list(range(0, numRows))
        while index < s_len:
            for item in group_count:
                if index < s_len:
                    if item < numRows:
                        if len(result_rows) <= item:
                            result_rows.append('')                    
                        result_rows[item] += s[index]
                    else:
                        result_rows[row_count[numRows-item - 2]] += s[index]
                index += 1
        result = ''
        for row in result_rows:
            result += row
        return result

# @lc code=end
