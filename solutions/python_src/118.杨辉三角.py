#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        pre_row = []
        for row_number in range(1, numRows + 1):
            current_row = []
            if row_number == 1:
                current_row = [1]
            else:
                for index in range(0, row_number):
                    if index == 0 or index == row_number - 1:
                        current_row.append(1)
                        continue
                    current_row.append(pre_row[index - 1] + pre_row[index])
            result.append(current_row)
            pre_row = current_row
        return result


# @lc code=end
