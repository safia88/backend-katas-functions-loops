#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    # your code here
    sum = x + y
    return sum


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if x > 0:
        num_times = x
    else:
        num_times = -x
    total = 0
    for i in range(num_times):
        total = add(total, y)
    # your code here
    if x < 0:
        total = -total
    return total


def power(x, n):
    """Raise x to power n, where n >= 0"""
    # your code here
    if n > 0:
        num_times = n
    else:
        num_times = -n
    total = x
    for i in range(num_times - 1):
        total = multiply(x, total)
    return total


def factorial(x):
    """Compute factorial of x, where x > 0"""
    # your code here
    result = 1
    for i in range(1, x + 1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


if __name__ == '__main__':
    # your code to call functions above
    print("The sum is", add(2, 4))
    print("The product is", multiply(6, -8))
    print("The power is", power(2, 8))
    print("The power is", factorial(4))
    print("The power is", fibonacci(8))
    # pass
