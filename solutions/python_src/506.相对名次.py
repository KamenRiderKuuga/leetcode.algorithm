#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
from operator import truediv


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_count = len(score)
        result = [None] * score_count
        rank_indexes = sorted(range(score_count), key=lambda i: score[i], reverse=True)
        for index in range(score_count):
            if index == 0:
                result[rank_indexes[index]] = "Gold Medal"
            elif index == 1:
                result[rank_indexes[index]] = "Silver Medal"
            elif index == 2:
                result[rank_indexes[index]] = "Bronze Medal"
            else:
                result[rank_indexes[index]] = str(index + 1)

        return result
# @lc code=end
