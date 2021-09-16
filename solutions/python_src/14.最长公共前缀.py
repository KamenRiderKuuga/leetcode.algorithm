#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 201
        has_min = False
        max_str = ""
        for item in strs:
            item_len = len(item)
            if item_len < min_len:
                min_len = item_len

        for index in range(0, min_len):
            current_char = ""
            for item in strs:
                if current_char == "":
                    current_char = item[index]
                elif current_char != item[index]:
                    has_min = True
                    break
            
            if has_min:
                break
            max_str += current_char
            
        return max_str        
# @lc code=end

