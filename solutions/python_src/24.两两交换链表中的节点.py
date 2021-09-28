#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        all_node = []
        input_node = head
        while head is not None:
            all_node.append(head)
            head = head.next
        for index in range(len(all_node)):
            if index % 2 == 0:
                if index + 3 < len(all_node):
                    all_node[index].next = all_node[index + 3]
                elif index + 2 < len(all_node):
                    all_node[index].next = all_node[index + 2]
                elif index + 1 < len(all_node):
                    all_node[index].next = None
            else:
                all_node[index].next = all_node[index - 1]

        if len(all_node) <= 1:
            return input_node
        else:
            return all_node[1]
# @lc code=end

