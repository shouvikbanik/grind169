from unittest import TestCase

from merge_two_sorted_lists import merge_two_sorted_lists


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Test(TestCase):
    def test_merge_two_sorted_lists(self):
        list1 = self.create_linked_list([0, 20, 40], False)
        list2 = self.create_linked_list([10, 30], False)
        list3 = self.create_linked_list([0, 10, 20, 30, 40], False)
        self.assertEqual(self.create_list_from_ll(merge_two_sorted_lists(list1, list2)),
                         self.create_list_from_ll(list3))

    def create_linked_list(self, elements, is_cyclic):
        head = ListNode()
        temp = head
        for element in elements:
            node = ListNode(element)
            if is_cyclic == True:
                node.next = head.next
            temp.next = node
            temp = node
        return head.next

    def create_list_from_ll(self, ll):
        return_list = []
        while (ll != None):
            return_list.append(ll.val)
            ll = ll.next
        return return_list
