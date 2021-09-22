#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        result = ''
        sum_value = 0
        plus_value = 0
        for index in range(max_len):
            a_value = 0
            b_value = 0
            if index < len(a):
                a_value = (1 if a[len(a) - 1 - index] == '1' else 0)
            if index < len(b):
                b_value = (1 if b[len(b) - 1 - index] == '1' else 0)

            sum_value = a_value + b_value + plus_value
            plus_value = 0
            if sum_value < 2:
                result = str(sum_value) + result
            else:
                plus_value = 1
                result = str(sum_value - 2) + result

        if plus_value == 1:
            result = "1" + result

        return result        
# @lc code=end

