#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = []
        column_hash = []
        square_hash = []
        for row_index in range(len(board)):
            row_hash.append(set())
            for column_index in range(len(board[row_index])):
                if len(column_hash) == column_index:
                    column_hash.append(set())
                square_index = int(row_index / 3) * 3 + int(column_index / 3)
                if len(square_hash) == square_index:
                    square_hash.append(set())
                value = board[row_index][column_index]
                if value == '.':
                    continue
                num_value = int(value)
                if num_value in row_hash[row_index]:
                    return False
                row_hash[row_index].add(num_value)
                if num_value in column_hash[column_index]:
                    return False
                column_hash[column_index].add(num_value)
                if num_value in square_hash[square_index]:
                    return False
                square_hash[square_index].add(num_value)
        return True
# @lc code=end
