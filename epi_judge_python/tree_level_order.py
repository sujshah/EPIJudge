from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque, namedtuple

NodeWithDepth = namedtuple("NodeWithDepth", ("element", "depth"))


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    result: List[List[int]] = []
    if not tree:
        return result
    queue = [tree]
    while queue:
        result.append([node.data for node in queue])
        queue = [
            child for node in queue for child in (node.left, node.right) if child
        ]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
