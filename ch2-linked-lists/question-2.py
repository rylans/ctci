'''Implement an algorithm to find the nth to last element of a singly linked list'''

class LinkedList(object):
    def __init__(self, val):
        self.next_node = None
        self.val = val

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        if node != None and type(node) != LinkedList:
            raise RuntimeError("Cannot link unknown type")
        self.next_node = node

def nth_to_last(head, n):
    '''Run a pointer n nodes forward, then start a second pointer
    Runs in O(n) time and constant space
    '''
    left_node = head
    right_node = head
    for i in xrange(n):
        if right_node.get_next() == None:
            raise RuntimeError("Linked list shorter than n")
        right_node = right_node.get_next()

    while right_node.get_next():
        left_node = left_node.get_next()
        right_node = right_node.get_next()

    return left_node

def make_list():
    A = LinkedList('A')
    B = LinkedList('B')
    C = LinkedList('C')
    D = LinkedList('D')
    C.set_next(D)
    B.set_next(C)
    A.set_next(B)
    return A

def test1():
    head = make_list()
    assert nth_to_last(head, 0).val == 'D'

def test2():
    head = make_list()
    assert nth_to_last(head, 1).val == 'C'

def test3():
    head = make_list()
    assert nth_to_last(head, 2).val == 'B'

if __name__ == '__main__':
    test1()
    test2()
    test3()
