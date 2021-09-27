#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_list = []
        while head is not None:
            node_list.append(head)
            head = head.next
        if len(node_list) < n:
            return None
        if len(node_list) == n:
            if len(node_list) > 1:
                return node_list[1]
            return None

        if n == 1:
            node_list[-n-1].next = None
        else:
            node_list[-n-1].next = node_list[-n + 1]

        return node_list[0]
# @lc code=end

