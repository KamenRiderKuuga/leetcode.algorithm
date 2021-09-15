#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        nums_set = set(map(lambda num: str(num), range(0, 10)))
        number_start = False
        result_arr = []
        nagative = False
        for item in s:
            if number_start:
                if item in nums_set:
                    result_arr.append(item)
                else:
                    break
            else:
                if item == '-':
                    nagative = True
                    number_start = True
                elif item == '+':
                    nagative = False
                    number_start = True
                elif item in nums_set:
                    number_start = True
                    result_arr.append(item)
                elif item != ' ':
                    return 0
        result = 0
        power = 0
        while len(result_arr) != 0:
            current_num = int(result_arr.pop())
            result += current_num * (10**power)
            power += 1
        if nagative:
            result = -result
        
        max_value = 2**31 - 1
        min_value = -2**31
        
        if result > max_value:
            result = max_value
        elif result < min_value:
            result = min_value
        return result
# @lc code=end
