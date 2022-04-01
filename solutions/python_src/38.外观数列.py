#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def Say(self, n) -> str:
        result = ""
        pre_num = ""
        count = 0
        for num in n:
            if num == pre_num:
                count += 1
            else:
                if pre_num != "":
                    result += f"{count}{pre_num}"
                count = 1
            pre_num = num
        result += f"{count}{pre_num}"
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.Say(self.countAndSay(n-1))
        # @lc code=end
