#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        value_list = [("M", 1000), ("D", 500), ("C", 100),
                    ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
        for couple in value_list:
            roman, value = couple
            while num >= value:
                num -= value
                result += roman
        result = result.replace("DCCCC", "CM").replace("CCCC", "CD").replace(
            "LXXXX", "XC").replace("XXXX", "XL").replace(
            "VIIII", "IX").replace("IIII", "IV")
        return result
# @lc code=end
