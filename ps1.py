import typing
import secrets
import random
import struct
import functools



def example(data: bytes) -> bytes:
    """
    Convert utf-8 encoded bytes to uppercase and return modified utf-8 encoded bytes

    >>> example(b'hello')
    b'HELLO'
    >>> example(b'hello').decode()
    'HELLO'
    >>> example('Ð¿Ñ€Ð¸Ð²Ñ–Ñ‚'.encode())
    b'\xd0\x9f\xd0\xa0\xd0\x98\xd0\x92\xd0\x86\xd0\xa2'
    >>> example('Ð¿Ñ€Ð¸Ð²Ñ–Ñ‚'.encode()).decode()
    'ÐŸÐ Ð˜Ð’Ð†Ð¢'
    """
    return data.decode("utf-8").upper().encode("utf-8")


def problem1(n: int) -> typing.List[int]:
    List = []
    while n != 0:
        List.append(secrets.choice(range(0,256)))
        #used https://docs.python.org/3/library/secrets.html
        #and https://stackoverflow.com/questions/32930246/python-for-loops-for-i-in-range0-lenlist-vs-for-i-in-list
        #and resource code provided by miroslav: https://github.com/cs-gy6903/resources
        n -= 1
    return List

    """
    Generate a list of `n` random numbers in range [0,256)

    Please use cryptographically-secure entropy source
    see secrets module in python

    # not doctest as output is random
    > problem1(5)
    [140, 7, 218, 46, 104]
    """
#problem1(14)

def problem2(n: int) -> bytes:
    return secrets.token_bytes(n)
    #used resource code provided by miroslav: https://github.com/cs-gy6903/resources
    """
    Generate random `n` bytes

    Please use cryptographically-secure entropy source
    see secrets module in python

    # not doctest as output is random
    > problem2(5)
    b'\x18s\x0b8B'
    """


def problem3(data: bytes) -> bytes:
    #used python docs: https://docs.python.org/3/library/stdtypes.html
    byte_list = []
    for x in list(data):
        new = x*2%256
        byte_list.append(new.to_bytes((new.bit_length() + 7) // 8, byteorder='little'))
        string = b''.join(byte_list)
    return(string)
        
 
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
    return bytes(functools.reduce(lambda a, b: a ^ b, i) for i in zip(*data))
    ##used resource code provided by miroslav: https://github.com/cs-gy6903/resources#xor-bytes
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
    return bytes.fromhex(data)
    ##used resource code provided by miroslav: https://github.com/cs-gy6903/resources#convert-hex-encoded-string-to-bytes

    """
    Decode given hex-encoded string to bytes

    >>> problem5('d0cad8d8de')
    b'\xd0\xca\xd8\xd8\xde'
    """


def problem6(data: bytes) -> str:
    return data.hex()
    #used resource code provided by miroslav: https://github.com/cs-gy6903/resources

    """
    Encode given bytes to hex-encoded string

    >>> problem6(b'hello')
    '68656c6c6f'
    """