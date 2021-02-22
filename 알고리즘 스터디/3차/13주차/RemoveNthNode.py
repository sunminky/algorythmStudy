#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(-1, head)
        fast_pointer = root
        slow_pointer = root

        for _ in range(n):
            #빠른 포인터는 느린 포인터보다 n노드 만큼 앞서 있음
            fast_pointer = fast_pointer.next

        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

        #n-1번째 노드와 n+1번째 노드를 연결
        slow_pointer.next = slow_pointer.next.next

        return root.next