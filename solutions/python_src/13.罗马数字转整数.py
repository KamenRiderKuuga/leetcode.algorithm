#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        last_index = len(s) - 1
        plus_value = 0
        jump = False
        for index in range(len(s)):
            if jump:
                jump = False
                continue
            if s[index] == 'I':
                plus_value = 1
                if index < last_index:
                    if s[index + 1] == "V":
                        plus_value = 4
                        jump = True
                    elif s[index + 1] == "X":
                        plus_value = 9
                        jump = True
            elif s[index] == "X":
                plus_value = 10
                if index < last_index:
                    if s[index + 1] == "L":
                        plus_value = 40
                        jump = True
                    elif s[index + 1] == "C":
                        plus_value = 90
                        jump = True
            elif s[index] == "C":
                plus_value = 100
                if index < last_index:
                    if s[index + 1] == "D":
                        plus_value = 400
                        jump = True
                    elif s[index + 1] == "M":
                        plus_value = 900
                        jump = True
            elif s[index] == "V":
                plus_value = 5
            elif s[index] == "L":
                plus_value = 50
            elif s[index] == "D":
                plus_value = 500
            elif s[index] == "M":
                plus_value = 1000
            
            result += plus_value
        
        return result

# @lc code=end
