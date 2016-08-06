'''
328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''
from data_structure.list_node import ListNode
from utilities.data_generator import *


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or not head.next or not head.next.next:
            return head

        odd_head = head
        even_head = head.next
        temp = head.next

        while even_head and even_head.next:
            odd_head.next = even_head.next
            even_head.next = even_head.next.next

            odd_head = odd_head.next
            even_head = even_head.next

        odd_head.next = temp

        return head


s = Solution()

head = generate_list([1, 2, 3, 4, 5])

head = s.oddEvenList(head)

print_list(head)
