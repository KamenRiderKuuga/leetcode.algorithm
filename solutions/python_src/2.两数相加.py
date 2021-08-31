#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_node = ListNode()
        loop_node = first_node
        exceed = 0
        while True:
            node1_value = 0
            node2_value = 0
            if l1 is not None:
                node1_value = l1.val
                l1 = l1.next
            if l2 is not None:
                node2_value = l2.val
                l2 = l2.next
            loop_node.val = node1_value + node2_value + loop_node.val
            if loop_node.val >= 10:
                loop_node.val -= 10
                loop_node.next = ListNode(1)
            if l1 is None and l2 is None:
                break

            if loop_node.next is None:
                loop_node.next = ListNode()
            loop_node = loop_node.next

        return first_node
# @lc code=end

