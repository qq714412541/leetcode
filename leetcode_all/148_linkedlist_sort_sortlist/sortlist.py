class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:###TLE  ###quick sort
    def sortList(self, head: ListNode) -> ListNode:
        return self.sort_node(head)

    def sort_node(self, node):
        #print('#')
        if not node:
            return None
        else:
            #print(node.val)
            new_node1, new_node2 = ListNode(0), ListNode('s')
            new_nodel, new_noder = ListNode(0), ListNode(0)
            new_nodel.next = new_node1
            new_noder.next = new_node2
            # new_node1.next = node
            pivot = node
            # new_node1 = new_node1.next
            while node.next:
                #print('???')
                if node.next.val < pivot.val:
                    new_node1.next = node.next
                    new_node1 = new_node1.next
                else:
                    new_node2.next = node.next
                    new_node2 = new_node2.next
                node = node.next
            #if new_node1.next:
            new_node1.next = None
            new_node2.next = None
            last = None if new_node2.val == 's' else new_node2

            last_l,new_nodel.next.next = self.sort_node(new_nodel.next.next)
            last_r,new_noder.next.next = self.sort_node(new_noder.next.next)
            return last,self.merge(new_nodel.next.next,last_l, pivot, new_noder.next.next)

    def merge(self, node1,last, pivot, node2):
        #print('?')
        new_node = ListNode(0)
        if node1:
            new_node.next = node1
            #print(node1.val)

            #print(node1.val)
            last.next = pivot

        else:
            new_node.next = pivot

        pivot.next = node2
        return new_node.next

new1 = ListNode(0)
#new2 = ListNode(0)
new1.next = ListNode(4)
new1.next.next = ListNode(2)
new1.next.next.next = ListNode(1)
new1.next.next.next.next = ListNode(3)

su = Solution()
res = su.sortList(new1)
print(res.val)



class Solution:#merge sort
    def sortList(self, head: ListNode) -> ListNode:
        #print(head.val)
        if not head or not head.next:
            return head
        else:
            slow = head
            fast = head.next
            while slow and  fast:
                if fast.next:
                    if fast.next.next:
                        fast = fast.next.next
                    else:
                        break
                else:
                    break
                slow = slow.next
            #print(slow.val)
            r = slow.next
            slow.next = None
            l = head
            l = self.sortList(l)
            r = self.sortList(r)
            return self.merge(l,r)

    def merge(self, h1,h2):
        pre = tail = ListNode(0)
        while h1 or h2:
            if not h2:
                pre.next = h1
                break
            elif not h1:
                pre.next = h2
                break
            elif h1.val>h2.val:
                pre.next = h2
                pre = pre.next
                h2 = h2.next
            else:
                pre.next = h1
                pre = pre.next
                h1 = h1.next
        return tail.next