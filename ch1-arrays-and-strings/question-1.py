from __future__ import print_function
'''
1.1 Implement an algorithm to determine if a string has all unique characters.
What if you can not user additional data structures?
'''

def check_unique(string):
    '''Using O(n) space and O(n) time'''
    charmap = {}

    for c in string:
        if c in charmap:
            return False
        else:
            charmap[c] = True
    return True

def check_unique_no_ds(string):
    '''No additional data structures
    Runs in constant space and O(n^2) time
    '''
    for ix in range(len(string)-1):
        char = string[ix]
        for char2 in string[ix+1:]:
            if char == char2:
                return False
    return True

def check_unique_sorted(string):
    '''No additional data structures. sort first
    Runs in O(n) space and O(n log n) time
    '''
    if len(string) < 2:
        return True
    sort_string = sorted(string)
    c1 = sort_string[0]
    for c in sort_string[1:]:
        if c == c1:
            return False
        c1 = c
    return True

def asserts(predicate, message):
    if not predicate:
        raise RuntimeError(message)
    print('.', end='')

if __name__ == '__main__':
    asserts(check_unique('abacad') == False, 'error for abacad')
    asserts(check_unique('jake') == True, 'error for jake')
    asserts(check_unique('jump up') == False, 'error on example 3')

    asserts(check_unique_no_ds('abacad') == False, 'error for example 4')
    asserts(check_unique_no_ds('jake') == True, 'error for example 5')
    asserts(check_unique_no_ds('jump up') == False, 'error on example 6')
    asserts(check_unique_no_ds('abra') == False, 'error on example 7')

    asserts(check_unique_sorted('abacad') == False, 'error for example 8')
    asserts(check_unique_sorted('jake') == True, 'error for example 9')
    asserts(check_unique_sorted('jump up') == False, 'error on example 10')
    asserts(check_unique_sorted('abra') == False, 'error on example 11')

    asserts(check_unique_sorted('x') == True, 'error on example 12')
    print('')
