#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For this assignment we will be using EC curve: y**2 = x**3 + ax + b (mod p)

https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication
"""
import typing

class P(typing.TypedDict):
    """
    Point on the EC

    We just care about x and y coordinates
    """

    x: int
    y: int


def multiplicative_inverse(i: int, p: int) -> int:
    """
    Compute multiplicative inverse of i for modulus p

    It needs to be smallest positive integer modular multiplicative inverse

    More on wikipedia:
    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    Hint you can use pow() built-in function

    >>> multiplicative_inverse(10, 17)
    12
    >>> multiplicative_inverse(5, 17)
    7
    """
    return  pow(i, -1, p)
    #reference: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

def point_negate(a: int, b: int, p: int, x: int, y: int) -> P:
    """
    Negate a point (x, y) on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_negation

    Remember all we are trying to do is to flip point around x-axis
    (flipping y coordinate) so we can sipmly use the formula:

    (x, -y) == -(x, y)

    >>> point_negate(a=2, b=3, p=17, x=5, y=11)
    {'x': 5, 'y': 6}
    """
    negate = P(x = x, y = (p - y))
    return negate

#print(point_negate(a=2, b=3, p=17, x=5, y=11))

def point_add(a: int, b: int, p: int, x1: int, y1: int, x2: int, y2: int) -> P:
    """
    Add point (x1, y1) to point (x2, y2) on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition

    You will need to compute the lambda (slope) which is:

    slope = y2 - y1
            -------
            x2 - x1

    Remember that instead of division we are multiplying by mod inverse.

    Then you can use slope to get the new point which is the result of the point
    addition:

    x = slope ** 2 - x1 - x2
    y = slope(x1 - x) - y1

    >>> point_add(a=2, b=3, p=17, x1=15, y1=5, x2=5, y2=11)
    {'x': 13, 'y': 4}
    >>> point_add(a=2, b=3, p=17, x2=15, y2=5, x1=5, y1=11)
    {'x': 13, 'y': 4}
    """
    return P(x=(((y2 - y1) * multiplicative_inverse((x2 - x1),p) % p)**2-x2-x1) % p, y=(((y2 - y1) * multiplicative_inverse((x2 - x1),p) % p)*(x2-(((y2 - y1) * multiplicative_inverse((x2 - x1),p) % p)**2-x2-x1) % p) - y2) % p)

#print(point_add(a=2, b=3, p=17, x1=15, y1=5, x2=5, y2=11))
#print(point_add(a=2, b=3, p=17, x2=15, y2=5, x1=5, y1=11))

def point_double(a: int, b: int, p: int, x: int, y: int) -> P:
    """
    Double (add to itself) a point (x, y) on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_doubling

    Doubling is similar to addtion except computing slope is different:

    slope = 3 * x1**2 + a
            -------------
            2 * y1

    >>> point_double(a=2, b=3, p=17, x=5, y=11)
    {'x': 15, 'y': 5}
    """
    return P(x=(((3 * (x**2) + a) * multiplicative_inverse(2 * y, p) % p)**2-x-x) % p,y=((((3 *(x**2)+a) * multiplicative_inverse(2 * y, p) % p)*(x-((((3 * (x**2) + a) * multiplicative_inverse(2 * y, p) % p)**2-x-x) % p))-y)) % p)

#print(point_double(a=2, b=3, p=17, x=5, y=11))




def point_multiply(a: int, b: int, p: int, x: int, y: int, n: int) -> P:
    """
    Multiply point (x, y) by n on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Double-and-add

    Now that we can:

    * negate points
    * double them
    * add 2 points

    we can implement point multiplication where multiplying by:

    * 1 == point itself
    * 2 == point double
    * x == point added x times. double and add method make this easy
    * -1 == point negation
    * -x == x * -1 (negate point and then multiply by positive multiplier)

    Instead of adding same point many-many times, double and add method should be used
    to make that operation much simpler. For example:
    p * 3 == p + p + p         == (p * 2) + p
    p * 5 == p + p + p + p + p == (p * 2) + (p * 2) + p == (p * 2) * 2 + p

    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=-1)
    {'x': 5, 'y': 6}
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=1)
    {'x': 5, 'y': 11}
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=2)
    {'x': 15, 'y': 5}
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=3)
    {'x': 13, 'y': 4}
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=4)
    {'x': 8, 'y': 15}
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=5)
    {'x': 2, 'y': 10}
    """
    def recursion(x,y,n): #P and N
        if abs(n) == 1:
            return P(x=x,y=y)
        elif n % 2:
            return point_add(a,b,p,x,y,recursion(x,y,abs(n)-1)['x'],recursion(x,y,abs(n)-1)['y'])  
        else:
            return recursion(point_double(a,b,p,x,y)['x'],point_double(a,b,p,x,y)['y'], abs(n) // 2)
    if n <= 0: #check for negative values 
        return point_negate(a,b,p,recursion(x,y,n)['x'],recursion(x,y,n)['y'])
    else: 
        return recursion(x,y,n) #go back recursively to handle remaining edge cases 
#refrence: https://github.com/cs-gy6903/2022-fall/blob/master/office-hours/will_2022-12-05.md
#https://stackoverflow.com/questions/21750977/checking-non-negative-even-integer-in-python
#https://github.com/cs-gy6903/resources#elliptic-curves
#https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction

 #f(P, d) is
 #    if d = 0 then
 #        return 0                         # computation complete
 #    else if d = 1 then
 #        return P
 #    else if d mod 2 = 1 then
 #        return point_add(P, f(P, d - 1)) # addition when d is odd
 #   else
 #        return f(point_double(P), d/2)   # doubling when d is even


#print(point_multiply(a=2, b=3, p=17, x=5, y=11, n=-1))
#print(point_multiply(a=2, b=3, p=17, x=5, y=11, n=1))
#print(point_multiply(a=2, b=3, p=17, x=5, y=11, n=2))
#print(point_multiply(a=2, b=3, p=17, x=5, y=11, n=3))
#print(point_multiply(a=2, b=3, p=17, x=5, y=11, n=4))
#print(point_multiply(a=2, b=3, p=17, x=5, y=11, n=5))
#print(point_multiply(a=26, b=51, p=59, x=7, y=24, n=-9))
#problem = Problem(input={'a': 26, 'b': 51, 'p': 59, 'x': 7, 'y': 24, 'n': -9}, output=None, reference={'x': 55, 'y': 1})

