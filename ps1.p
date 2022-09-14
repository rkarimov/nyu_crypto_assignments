import typing
import secrets
import random


def example(data: bytes) -> bytes:
    """
    Convert utf-8 encoded bytes to uppercase and return modified utf-8 encoded bytes

    >>> example(b'hello')
    b'HELLO'
    >>> example(b'hello').decode()
    'HELLO'
    >>> example('привіт'.encode())
    b'\xd0\x9f\xd0\xa0\xd0\x98\xd0\x92\xd0\x86\xd0\xa2'
    >>> example('привіт'.encode()).decode()
    'ПРИВІТ'
    """
    return data.decode("utf-8").upper().encode("utf-8")


def problem1(n: int) -> typing.List[int]:
    List = []
    while n != 0:
        List.append(secrets.choice(range(0,256)))
        n -= 1
    print(List)

    """
    Generate a list of `n` random numbers in range [0,256)

    Please use cryptographically-secure entropy source
    see secrets module in python

    # not doctest as output is random
    > problem1(5)
    [140, 7, 218, 46, 104]
    """
problem1(5)

def problem2(n: int) -> bytes:
    print(secrets.token_bytes(n))
    """
    Generate random `n` bytes

    Please use cryptographically-secure entropy source
    see secrets module in python

    # not doctest as output is random
    > problem2(5)
    b'\x18s\x0b8B'
    """

problem2(5)


def problem3(data: bytes) -> bytes:
    """
    Manipulate given data bytes where each byte is multiplied * 2 % 256

    In other words, input is a collection of bytes
    You should multiply each of those bytes by 2 mod 256
    (not to overflow)
    and then return resulting bytes

    >>> problem3(b'hello')
    b'\xd0\xca\xd8\xd8\xde'
    """


def problem4(data: typing.List[bytes]) -> bytes:
    """
    XOR all given bytes and output resulting XORed bytes

    All inputs will be of same length

    >>> problem4([
    ...     b'hello',
    ...     b'world',
    ...     b'hello',
    ... ])
    b'world'
    """


def problem5(data: str) -> bytes:
    """
    Decode given hex-encoded string to bytes

    >>> problem5('d0cad8d8de')
    b'\xd0\xca\xd8\xd8\xde'
    """


def problem6(data: bytes) -> str:
    """
    Encode given bytes to hex-encoded string

    >>> problem6(b'hello')
    '68656c6c6f'
    """
