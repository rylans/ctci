from __future__ import print_function
import doctest
'''Given a sorted (increasing order) array, write an algorithm to create
a binary tree with minimal height.'''

class BiTree(object):
    def __init__(self, value):
        self._val = value
        self.left_child = None
        self.right_child = None

    def value(self):
        return self._val

    def __repr__(self):
        return self._repr_helper('')

    def _repr_helper(self, s):
        s += str(self.value())
        if self.left_child:
            s += str(self.left_child)
        if self.right_child:
            s += str(self.right_child)
        return s

    def preorder(self):
        print(self.value(), end='')
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

def tree_from_array(arr):
    '''
    Build a tree from array

    >>> tree_from_array([1,2,3,4]).preorder()
    3214

    >>> tree_from_array([1,2,3,4,5]).preorder()
    32154

    >>> tree_from_array([1,2,3]).preorder()
    213
    '''
    mid = len(arr)/2
    lefthalf = arr[:mid]
    righthalf = arr[mid+1:]
    node = BiTree(arr[mid])
    if lefthalf:
        node.left_child = tree_from_array(lefthalf)
    if righthalf:
        node.right_child = tree_from_array(righthalf)
    return node

if __name__ == '__main__':
    doctest.testmod()
