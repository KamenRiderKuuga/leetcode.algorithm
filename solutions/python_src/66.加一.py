#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = True
        result = []
        for num in list(reversed(digits)):
            if plus:
                if num != 9:
                    num += 1
                    plus = False
                else:
                    num = 0
                    plus = True
            result.append(num)
        if plus:
            result.append(1)
        return list(reversed(result))

# @lc code=end

