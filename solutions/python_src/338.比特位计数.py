#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            count = 0
            while num != 0:
                (num, remainder) = divmod(num, 2)
                if remainder != 0:
                    count += 1
            result.append(count)
        return result

# @lc code=end
