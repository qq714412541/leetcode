# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        testA = headA
        testB = headB
        countA = 0
        countB = 0
        arrA = []
        arrB = []
        while testA:
            countA += 1
            arrA = [testA.val] + arrA
            testA = testA.next
        while testB:
            countB += 1
            arrB = [testB.val] + arrB
            testB = testB.next
        count = 0
        while arrA and arrB:
            if arrA[0] == arrB[0]:
                count += 1
                arrA = arrA[1:]
                arrB = arrB[1:]
            else:
                break

        if count == 0:
            # print('??')
            return None
        else:
            countA -= count
            countB -= count
        # print(countA,countB)
        while countA > 0:
            headA = headA.next
            countA -= 1
        while countB > 0:
            headB = headB.next
            countB -= 1
        while headA and headB:
            if headA == headB:
                # print('??????')
                return headA
            else:
                headA = headA.next
                headB = headB.next
        # print('?')
        return None


class Solution:#stack
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        stackA = []
        stackB = []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        #temp = 0
        if not stackA or not stackB:
            return None
        if stackA[-1] != stackB[-1]:
            return None
        while stackA and stackB:
            x = stackA.pop()
            y = stackB.pop()
            if x == y:
                temp = x
                if not stackB or not stackA:
                    return temp
                else:
                    continue
            else:
                return temp



class Solution:#有情人终成眷属法
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        newA = headA
        newB = headB
        while True:
            if not headA or not headB:
                return None
            if headA == headB:
                return headA
            else:
                headA = headA.next
                if not headA:
                    headA = newB
                    newB = None
                headB = headB.next
                if not headB:
                    headB = newA
                    newA = None