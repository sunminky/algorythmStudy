# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast_pointer = head  # 2칸씩 이동하는 포인터
        slow_pointer = head  # 1칸씩 이동하는 포인터

        while fast_pointer:
            # 빠른 포인터 2칸 이동
            for i in range(2):
                # 리스트의 끝을 만남(사이클이 존재하지 않음)
                if fast_pointer.next is None:
                    #리스트의 길이가 홀수 인 경우
                    if i & 1:
                        return slow_pointer.next
                    #리스트의 길이가 짝수 인 경우
                    else:
                        return slow_pointer
                else:
                    fast_pointer = fast_pointer.next

            # 느린 포인터 1칸 이동
            slow_pointer = slow_pointer.next