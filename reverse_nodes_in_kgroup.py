# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReverseKNodes(object):
    def move_ahead(self, original, k):
        for i in range(k-1):
            original = original.next
            if not original:
                return False
        return True

    def swap_nodes(self, preva, a, prevb, b):
        tmp = ListNode(0)
        # replace a with tmp
        tmp.next = a.next
        preva.next = tmp
        # replace b with a



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
        front = head
        back = head
        for i in range(k-1):
            head = head.next
        while True:
            for i in range(k-1):
                back = back.next
                if not back:
                    return head
            # connect prev to the second node
            prev.next = front.next
            # insert front behind back
            front.next = back.next
            back.next = front
            # update front and back and prev
            prev = front
            front = front.next
            back = front
            if not back:
                break
        return head


if __name__ == '__main__':
    head = ListNode(1)
    p = head
    for i in range(2):
        p.next = ListNode(i+2)
        p = p.next
    rnk = ReverseKNodes()
    result = rnk.reverseKGroup(head, 3)
