from __future__ import print_function
'''Implement a function to check if a tree is balanced. For the purposes of this
question, a balanced tree is defined to be a tree such that no two leaf nodes differ
in distance from the root by more than one'''

class BiTree(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def max_d(root, d):
    if not root:
        return d
    left = max_d(root.left_child, d+1)
    right = max_d(root.right_child, d+1)
    return max(left, right)

def min_d(root, d):
    if not root:
        return d
    left = min_d(root.left_child, d+1)
    right = min_d(root.right_child, d+1)
    return min(left, right)

def is_balanced(root):
    '''Balanced if max_depth - min_depth < 2'''
    if not root:
        return True
    if (max_d(root, 0) - min_d(root, 0)) < 2:
        return True
    return False

def get_balanced():
    A = BiTree('A')
    B = BiTree('B')
    C = BiTree('C')
    D = BiTree('D')
    A.left_child = B
    A.right_child = C
    C.left_child = D
    return A

def get_unbalanced():
    A = BiTree('A')
    B = BiTree('B')
    C = BiTree('C')
    D = BiTree('D')
    E = BiTree('E')
    F = BiTree('F')
    A.left_child = B
    A.right_child = C
    C.left_child = D
    C.right_child = F
    D.right_child = E

    return A

def asserts(predicate, message):
    if not predicate:
        raise RuntimeError(message)
    print('.', end='')

if __name__ == '__main__':
    asserts(is_balanced(get_balanced())==True, "test 1 failed")
    asserts(is_balanced(get_unbalanced())==False, "test 2 failed")
    print('')
