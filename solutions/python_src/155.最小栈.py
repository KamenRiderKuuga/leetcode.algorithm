#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    class ListNode:
        def __init__(self, x, min):
            self.val = x
            self.min = min
            self.next = None

    def __init__(self):
        self.firstNode = self.ListNode(None, None)

    def push(self, val: int) -> None:
        min = self.getMin()
        if min is None or val < min:
            min = val
        node = self.ListNode(val, min)
        node.next = self.firstNode
        self.firstNode = node

    def pop(self) -> None:
        self.firstNode = self.firstNode.next

    def top(self) -> int:
        return self.firstNode.val

    def getMin(self) -> int:
        return self.firstNode.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
