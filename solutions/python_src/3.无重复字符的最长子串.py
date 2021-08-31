#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic_of_str = {}
        start_index = 0
        current_index = 0
        max_length = 0
        for item in s:
            if item in dic_of_str.keys():
                if start_index <= dic_of_str[item]:
                    start_index = dic_of_str[item] + 1
            dic_of_str[item] = current_index
            current_index += 1
            current_length = current_index - start_index
            max_length = current_length if current_length > max_length else max_length
        return max_length

# @lc code=end
