def reverse_linked_list(head):
    if not head or not head.next:
        return head
    ptr1, ptr2 = None, head
    while ptr2:
        ptr3 = ptr2.next
        ptr2.next = ptr1
        ptr1 = ptr2
        ptr2 = ptr3
    return ptr1
