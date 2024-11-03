from unittest import TestCase

from lowest_common_ancestor_of_binary_tree import lowest_common_ancestor


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Test(TestCase):
    def test_lowest_common_ancestor(self):
        node1 = TreeNode(6)
        node2 = TreeNode(2)
        node3 = TreeNode(8)
        node4 = TreeNode(0)
        node5 = TreeNode(4)
        node6 = TreeNode(7)
        node7 = TreeNode(9)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7

        self.assertEqual(lowest_common_ancestor(node1, node2, node3).val, node1.val)
