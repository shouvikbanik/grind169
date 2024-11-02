class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1, list2):
    head = ListNode(0, None)
    temp_head = head
    while list1 and list2:
        if list1.val < list2.val:
            temp_head.next = list1
            temp_head = temp_head.next
            list1 = list1.next
        else:
            temp_head.next = list2
            temp_head = temp_head.next
            list2 = list2.next
    if list1:
        temp_head.next = list1
    elif list2:
        temp_head.next = list2
    return head.next
