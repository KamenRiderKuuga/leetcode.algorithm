#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "{":
                stack.append("}")
            elif item == "[":
                stack.append("]")
            elif len(stack) == 0 or item != stack.pop():
                return False
        return len(stack) == 0        
# @lc code=end

