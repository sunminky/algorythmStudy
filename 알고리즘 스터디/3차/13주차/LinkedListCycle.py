#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast_pointer = head #2칸씩 이동하는 포인터
        slow_pointer = head #1칸씩 이동하는 포인터

        while fast_pointer and slow_pointer:
            #빠른 포인터 2칸 이동
            for _ in range(2):
                #리스트의 끝을 만남(사이클이 존재하지 않음)
                if fast_pointer.next is None:
                    return False
                else:
                    fast_pointer = fast_pointer.next

            #느린 포인터 1칸 이동
            slow_pointer = slow_pointer.next

            #느린포인터와 빠른포인터가 만난 경우(사이클 존재)
            if fast_pointer == slow_pointer:
                return True