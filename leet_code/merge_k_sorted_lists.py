'''

23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

'''

from data_structure.list_node import ListNode
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))

        heapq.heapify(heap)
        head = ListNode(0);
        curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]

        mid = length / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return None

        if not l2:
            return l1
        elif not l1:
            return l2

        res = ListNode(0)
        head = res

        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next

        res.next = l1 or l2

        return head.next