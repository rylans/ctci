from __future__ import print_function
'''Write a method to replace all spaces in a string with "%20"
'''

def escape_space(string):
    '''Runs in O(n) time and space'''
    new_string = ''
    for char in string:
        if char == ' ':
            new_string += '%20'
        else:
            new_string += char
    return new_string

def asserts(predicate, message):
    if not predicate:
        raise RuntimeError(message)
    print('.', end='')

if __name__ == '__main__':
    asserts(escape_space('abra cadabra') == "abra%20cadabra", 'example 1 failed')
    asserts(escape_space(' starts') == "%20starts", 'example 2 failed')
    asserts(escape_space('ends ') == "ends%20", 'example 3 failed')
    asserts(escape_space('consecutive  ones .') == "consecutive%20%20ones%20.", 'example 4 failed')
    print('')
