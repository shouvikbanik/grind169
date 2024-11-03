def linked_list_cycle(head):
    sptr = head
    if not sptr:
        return False
    fptr = sptr.next
    while fptr and fptr.next:
        fptr = fptr.next.next
        sptr = sptr.next
        if sptr == fptr:
            return True
    return False
