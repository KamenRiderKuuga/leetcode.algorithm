#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = {}
        mapped = set()
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            if s[index] not in mapper.keys():
                if t[index] not in mapped:
                    mapper[s[index]] = t[index]
                    mapped.add(t[index])
                else:
                    return False
            else:
                if mapper[s[index]] != t[index]:
                    return False
        return True
# @lc code=end
