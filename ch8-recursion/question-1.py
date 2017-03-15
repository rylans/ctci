'''Write a method to generate the nth Fibonacci number.'''
import doctest

def nth_fib(n):
    '''Return the nth fibonacci number. Memoized

    >>> nth_fib(3)
    2

    >>> nth_fib(4)
    3

    >>> nth_fib(100)
    354224848179261915075L
    '''
    return _nth_fib_memoized(n)

def _nth_fib_memoized(n, mem={}):
    if n < 1:
        raise RuntimeError("n must be 1 or greater")
    if n == 1:
        return 1
    if n == 2:
        return 1

    if mem.get(n):
        return mem[n]

    n_minus_1 = _nth_fib_memoized(n - 1)
    n_minus_2 = _nth_fib_memoized(n - 2)

    nfib = n_minus_1 + n_minus_2
    mem[n] = nfib
    return nfib

if __name__ == '__main__':
    doctest.testmod()
