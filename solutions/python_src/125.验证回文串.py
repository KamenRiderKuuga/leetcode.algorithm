#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = 0
        len_s = len(s)
        max_index = len_s - 1
        while left_index + right_index <= len_s:
            while left_index < max_index and not s[left_index].isalnum():
                left_index += 1
            while right_index < max_index and not s[len_s - 1 - right_index].isalnum():
                right_index += 1
            if s[left_index].lower() != s[max_index - right_index].lower():
                if s[left_index].isalnum() and s[max_index - right_index].isalnum():
                    return False
            left_index += 1
            right_index += 1

        return True
# @lc code=end

