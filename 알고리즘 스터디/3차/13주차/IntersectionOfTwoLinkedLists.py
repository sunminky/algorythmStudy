# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        spendA = False  #노드 A가 자신의 리스트를 다 순회 했는지지 체크
        spendB = False  #노드 B가 자신의 리스트를 다 순회 했는지 체크
        
        #노드 A와 노드B가 전부 None이 아닐때 까지 탐색
        while nodeA and nodeB:
            #노드 A와 노드 B가 만남(사이클 존재)
            if nodeA == nodeB:
                return nodeA

            nodeA = nodeA.next
            nodeB = nodeB.next

            #노드 A가 자신의 리스트를 전부 순회한 경우 노드 B를 순회하도록 함
            if nodeA is None and not spendA:
                nodeA = headB
                spendA = True
            # 노드 B가 자신의 리스트를 전부 순회한 경우 노드 A를 순회하도록 함
            if nodeB is None and not spendB:
                nodeB = headA
                spendB = True

        #두 노드가 서로 만나지 못하고 종료한 경우(사이클 없음)
        return None