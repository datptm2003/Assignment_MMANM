import random
import struct
import time
import math

from my_rsa.sieve_base import sieve_base

random.seed(time.time())
randfunc = random.randint

def bytes_to_long(b):
    acc = 0
    unpack = struct.unpack
    length = len(b)
    if length % 4:
        extra = (4 - length % 4)
        b = b'\x00' * extra + b
        length = length + extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack('>I', b[i:i + 4])[0]
    return acc

def long_to_bytes(n, blocksize=0):
    """Convert a positive integer to a byte string using big endian encoding.
    If :data:`blocksize` is absent or zero, the byte string will be of minimal length.
    Otherwise, the length of the byte string is guaranteed to be a multiple of :data:`blocksize`. 
    If necessary, zeroes (``\\x00``) are added at the left.
    """
    if n < 0 or blocksize < 0:
        raise ValueError("Values must be non-negative")
    result = []
    pack = struct.pack
    # Fill the first block independently from the value of n
    bsr = blocksize
    while bsr >= 8:
        result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
        n = n >> 64
        bsr -= 8
    while bsr >= 4:
        result.insert(0, pack('>I', n & 0xFFFFFFFF))
        n = n >> 32
        bsr -= 4
    while bsr > 0:
        result.insert(0, pack('>B', n & 0xFF))
        n = n >> 8
        bsr -= 1
    if n == 0:
        if len(result) == 0:
            bresult = b'\x00'
        else:
            bresult = b''.join(result)
    else:
        # The encoded number exceeds the block size
        while n > 0:
            result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
            n = n >> 64
        result[0] = result[0].lstrip(b'\x00')
        bresult = b''.join(result)
        # bresult has minimum length here
        if blocksize > 0:
            target_len = ((len(bresult) - 1) // blocksize + 1) * blocksize
            bresult = b'\x00' * (target_len - len(bresult)) + bresult
    return bresult

def str_to_long(s):
    """Convert a string to a long number."""
    if type(s) is not str:
        raise ValueError("The input must be a string.")
    return bytes_to_long(s.encode())

def size_in_bits(n):
    """Returns the size of the number n in bits."""
    if n < 0:
        raise ValueError("Size in bits only available for non-negative numbers")
    return n.bit_length()

def random_with_n_bits(n_bits):
    """Return a random number with exactly n-bits.
    """
    if n_bits <= 0:
        raise ValueError("Number of bits must be positive.")
    min_val = 2**(n_bits - 1)
    max_val = 2**n_bits - 1
    return randfunc(min_val, max_val)

def random_at_most_n_bits(n_bits):
    """Return a random number with at most n-bits.
    """
    if n_bits <= 0:
        raise ValueError("Number of bits must be positive.")
    min_val = 0
    max_val = 2**n_bits - 1
    return randfunc(min_val, max_val)

def random_in_range(a, b):
    """Return a random number in range [a,b].
    """
    return randfunc(a, b)

def inverse(u, v):
    """The inverse of :data:`u` *mod* :data:`v`."""
    if v == 0:
        raise ZeroDivisionError("Modulus cannot be zero")
    if v < 0:
        raise ValueError("Modulus cannot be negative")
    
    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q = u3 // v3
        u1, v1 = v1, u1 - v1*q
        u3, v3 = v3, u3 - v3*q
    if u3 != 1:
        raise ValueError("No inverse value can be computed")
    while u1 < 0:
        u1 = u1 + v
    return u1

def gcd(x,y):
    """Greatest Common Divisor of :data:`x` and :data:`y`.
    """
    x = abs(x)
    y = abs(y)
    while x > 0:
        x, y = y % x, x
    return y

def power(a, p, mod):
    if a % mod == 0:
        return 0
    if p == 0:
        return 1
    if p == 1:
        return a % mod
    remain = 1
    while True:
        if p % 2 == 0:
            p = p >> 1
        else:
            p = (p-1) >> 1
            remain = (remain * a) % mod
        a = (a**2) % mod
        if p == 1:
            return (a * remain) % mod

def is_prime(n, false_positive_prob=1e-6):
    """Test if a number n is a prime.
    """
    if n < 3 or n & 1 == 0:
        return n == 2
    for p in sieve_base:
        if n == p:
            return True
        if n % p == 0:
            return False
    rounds = int(math.ceil(-math.log(false_positive_prob)/math.log(4)))
    return bool(__rabin_miller_test__(n, rounds))

def __rabin_miller_test__(n, rounds):
    """_rabinMillerTest(n:long, rounds:int, randfunc:callable):int
    Tests if n is prime.
    Returns 0 when n is definitely composite.
    Returns 1 when n is probably prime.
    Returns 2 when n is definitely prime.
    """
    # check special cases (n==2, n even, n < 2)
    if n < 3 or (n & 1) == 0:
        return n == 2
    # n might be very large so it might be beneficial to precalculate n-1
    n_1 = n - 1
    # determine m and b so that 2**b * m = n - 1 and b maximal
    b = 0
    m = n_1
    while (m & 1) == 0:
        b += 1
        m >>= 1
    tested = []
    # we need to do at most n-2 rounds.
    for i in range(min(rounds, n-2)):
        # randomly choose a < n and make sure it hasn't been tested yet
        a = random_in_range(2, n)
        while a in tested:
            a = random_in_range(2, n)
        tested.append(a)
        # do the rabin-miller test
        z = power(a, m, n)  # (a**m) % n
        if z == 1 or z == n_1:
            continue
        composite = 1
        for r in range(b):
            z = (z * z) % n
            if z == 1:
                return 0
            elif z == n_1:
                composite = 0
                break
        if composite:
            return 0
    return 1

def random_prime_with_n_bits(n_bits):
    """Return a random N-bit prime number.
    N must be an integer larger than 1.
    """
    if n_bits < 2:
        raise ValueError("N must be larger than 1")
    while True:
        number = random_with_n_bits(n_bits) | 1
        if is_prime(number):
            break
    return number
