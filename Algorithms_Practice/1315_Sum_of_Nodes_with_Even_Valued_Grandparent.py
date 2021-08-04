# Given binary tree, return the sum of values of nodes, with event-valued grandparent.
# (A grandparent of the node is the parent of its parent, if it exits)
# If there are no nodes with an even-valued grandparent, return 0
from collections import deque
from math import floor


# geeks for geeks
def buildTree(ip):
    # create the root of the tree
    root = TreeNode(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # starting from second element
    i = 1
    while size > 0 and i < len(ip):
        # get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # get the current nodes value from the string
        currVal = ip[i]

        # if the left child is not null
        if currVal != 'N':
            # create the left child for the current node
            currNode.left = TreeNode(int(currVal))

            # push it to queue
            q.append(currNode.left)
            size = size + 1

        # for the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # if the right child is not null
        if currVal != 'N':
            # create the right child for the current node
            currNode.right = TreeNode(int(currVal))

            # push it to queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1

    return root


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level=level + 1)
        print(3 * '' * level + str(node.val))
        print_tree(node.left, level=level + 1)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def sumEvenGrandParent(self, root: TreeNode) -> int:
        level_order = self.printLevelOrder(root)
        print(level_order)
        answer = 0

        for i in range(len(level_order)):
            parent = floor((i - 1) / 2)
            grandparent = floor((parent - 1) / 2)
            print(level_order[i], parent, grandparent)

            if grandparent >= 0 and level_order[grandparent] != 'N' and level_order[grandparent] % 2 == 0:
                if level_order[i] != 'N':
                    answer += level_order[i]
        return answer

    def printLevelOrder(self, root):
        # base case
        if root is None:
            return
        # create an empty queue for level order traversal
        queue = []
        # enqueue root and initialize height
        queue.append(root)
        level_order = []
        while len(queue) > 0:
            # print front on queue and remove it from queue
            # print(queue[0].val)
            if queue[0] == 'N':
                level_order.append('N')
                queue.pop(0)
                continue

            if queue[0].val is not None:
                level_order.append(queue[0].val)

            node = queue.pop(0)

            # enqueue left child
            if node.left is not None:
                queue.append(node.left)
            else:
                queue.append('N')

            # enqueue right child
            if node.right is not None:
                queue.append(node.right)
            else:
                queue.append('N')
        return level_order


if __name__ == '__main__':
    # tree_repr = [6, 7, 8, 2, 7, 1, 3, 9, 'N', 1, 4, 'N', 'N', 'N', 5]
    tree_repr = [50, 'N', 54, 98, 6, 'N', 'N', 'N', 34]
    root = buildTree(tree_repr)
    # print_tree(root)
    print(Solution().sumEvenGrandParent(root))
