#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        letters = sentence.split(' ')
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = ' '.join((l + "ma" + "a" * i) if l[0].lower() in vowels else (
            (l + l[0])[1:] + "ma" + "a" * i) for i, l in enumerate(letters, 1))
        return result
# @lc code=end
