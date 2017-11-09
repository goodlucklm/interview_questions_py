# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class ReverseKNodes(object):
    def move_ahead(self, original, k):
        for i in range(k):
            original = original.next
            if not original:
                return None
        return original

    def swap_nodes(self, preva, prevb):
        if not preva or not prevb :
            return None
        a = preva.next
        b = prevb.next
        if not a or not b:
            return None

        tmp = ListNode(0)
        preva.next = b
        prevb.next = a
        tmp.next = a.next
        a.next = b.next
        b.next = tmp.next
        return True

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # empty list or single item list
        if not head or not head.next:
            return head

        # reverse 1 item
        if k == 1:
            return head

        prev = ListNode(0)
        prev.next = head
        head = self.move_ahead(head, k-1)
        if not head:
            return prev.next

        while True:
            front = prev  # point front.next is the node to swap
            back = prev  # back.next is the node to swap
            back = self.move_ahead(back, k-1)
            if not back or not back.next:
                break
            for i in range(1, (k >> 1)+1):
                self.swap_nodes(front, back)
                # update front, back
                front = front.next
                back = self.move_ahead(front, k-2*i-1)
            prev = self.move_ahead(prev, k)
            if not prev:
                break
        return head


if __name__ == '__main__':
    head = ListNode(1)
    p = head
    for i in range(5):
        p.next = ListNode(i+2)
        p = p.next
    rnk = ReverseKNodes()
    result = rnk.reverseKGroup(head, 6)
    print result
