'''Write code to remove duplicates from an unsorted linked list'''

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

    @staticmethod
    def iterate_over(head):
        string = ""
        if not head:
            return string
        string += head.val
        nex = head.get_next()
        while nex:
            string += nex.val
            nex = nex.get_next()
        return string

def remove_dups(head):
    seen_vals = {}
    node = head
    last = None
    while node.get_next():
        if seen_vals.get(node.val):
            last.set_next(node.get_next())
        else:
            seen_vals[node.val] = node.val
            last = node
        node = node.get_next()

    if seen_vals.get(last.get_next().val):
        last.set_next(None)

if __name__ == '__main__':
    A = LinkedList('A')
    B = LinkedList('B')
    C = LinkedList('C')
    A2 = LinkedList('A')
    C.set_next(A2)
    B.set_next(C)
    A.set_next(B)
    remove_dups(A)
    print LinkedList.iterate_over(A)
