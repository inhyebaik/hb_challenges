class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and its successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))

def add_linked_lists(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format (4,5,6 -> 6,5,4,None)
    l2: the head node of another "reverse-digit" format (1,2,3 -> 3,2,1, None)

    Returns: head node of linked list of sum in "reverse-digit" format. (123+456 = 579)
    """

    curr1 = l1
    curr2 = l2
    result = None

    while curr1 and curr2:
        _sum = curr1.data + curr2.data

        if (_sum) > 9:
            _sum -= 10
            curr1.next.data + 1

        if not result:
            result = Node(_sum)
        else:
            result.next = Node(_sum)
        _sum = 0 

        curr1 = curr1.next
        curr2 = curr2.next

    result.next = None
    return result

def add_linked_lists2(l1, l2):
    """Given two linked lists, treat like numbers and add together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # START SOLUTION

    out_head = out_tail = None
    carried_over_digit = 0

    # Loop over both lists stopping when *both* lists are done

    while l1 or l2:

        # If not done l1, get digit, move to next. If done, use 0.

        if l1:
            digit1 = l1.data
            l1 = l1.next
        else:
            digit1 = 0

        # If not done l2, get digit, move to next. If done, use 0.

        if l2:
            digit2 = l2.data
            l2 = l2.next
        else:
            digit2 = 0

        # Add together digits (along w/carry) & determine new carry

        new_digit = digit1 + digit2 + carried_over_digit
        carried_over_digit, new_digit = divmod(new_digit, 10)

        # Add to end of our out LL

        if not out_head:
            out_head = out_tail = Node(new_digit)

        else:
            out_tail.next = Node(new_digit)
            out_tail = out_tail.next

    # If we have any carry left over, add a new place for it

    if carried_over_digit:
        out_tail.next = Node(carried_over_digit)

    return out_head


l1 =  Node(3, Node(2, Node(1))) 
l2 =  Node(6, Node(4, Node(5))) 

print add_linked_lists(l1, l2)
print add_linked_lists2(l1, l2)










