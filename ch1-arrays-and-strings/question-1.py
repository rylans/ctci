from __future__ import print_function
'''
1.1 Implement an algorithm to determine if a string has all unique characters.
What if you can not user additional data structures?
'''

def check_unique(string):
    charmap = {}

    for c in string:
        if c in charmap:
            return False
        else:
            charmap[c] = True
    return True


def asserts(predicate, message):
    if not predicate:
        raise RuntimeError(message)
    print('.', end='')

if __name__ == '__main__':
    asserts(check_unique('abacad') == False, 'error for abacad')
    asserts(check_unique('jake') == True, 'error for jake')
    asserts(check_unique('jump up') == False, 'error on example 3')
    print('')
