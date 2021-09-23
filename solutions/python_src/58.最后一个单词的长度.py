#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        started = False
        result = 0
        while len_s != 0:
            len_s -= 1
            current_value = s[len_s]
            if started == False and current_value != ' ':
                started = True
            if started:
                if current_value != ' ':
                    result += 1
                else:
                    break

        return result        
# @lc code=end

