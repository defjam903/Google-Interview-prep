class LinkedListMode:
    def __init__(self, value):
        self.vale = value
        self.next = None


def reverse(head_of_list):
    current = head_of_list
    previous = None
    next = None
    # until we have 'fallen off' the end of the list
    while current:
        # copy a pointer to the next element
        # before we overwrite current.next
        next = current.next
        # reverse the 'next' pointer
        current.next = previous
        # step forward in the list
        previous = current
        current = next
    return previous


