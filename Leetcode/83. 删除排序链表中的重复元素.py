# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # solution 1
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        elements = []
        cur = head
        while cur:
            elements.append(cur.val)
            cur = cur.next

        elements = list(set(elements))
        elements.sort()

        new_head = ListNode(elements[0])
        pointer = new_head
        for element in elements[1:]:
            pointer.next = ListNode(element)
            pointer = pointer.next
        return new_head

    # solution 2
    def deleteDuplicates_v2(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

