__author__ = 'John Underwood'

# Fibonacci numbers module - experiment with functional programming


def fib(n):    # write Fibonacci series up to n
    """
    :param n: takes any integer.
    :return: prints each item in the fibonacci sequence
    """
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b


def fib2(n):  # return Fibonacci series up to n
    """
    :param n: takes any integer.
    :return: a fibonacci sequence list
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


def fib_final(n):
    """
    :param n: takes any integer.
    :return: final value of the fibonacci sequence
    """
    return fib2(n)[-1:]