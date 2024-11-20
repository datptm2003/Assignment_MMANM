import my_rsa.utils as utils
from my_rsa import RSA

import time

class Result:
    def __init__(self, **args):
        self.__dict__ = args

    def show(self):
        return self.__dict__

def find_random_prime(rsa: RSA, n_bits):
    start_time = time.time()
    prime = utils.random_prime_with_n_bits(n_bits)
    end_time = time.time()

    return Result(prime=prime), end_time - start_time

def find_gcd(rsa: RSA, a, b):
    start_time = time.time()
    gcd = utils.gcd(a, b)
    end_time = time.time()

    return Result(gcd=gcd), end_time - start_time

def find_d(rsa: RSA, p, q, e):
    start_time = time.time()
    rsa.set_p(p)
    rsa.set_q(q)
    d = rsa.d
    end_time = time.time()

    return Result(d=d), end_time - start_time

def find_keys(rsa: RSA, p, q):
    start_time = time.time()
    rsa.set_p(p)
    rsa.set_q(q)
    n = rsa.n
    e = rsa.e
    d = rsa.d
    end_time = time.time()

    return Result(n=n, e=e, d=d), end_time - start_time

def encrypt(rsa: RSA, plaintext, n, e):
    start_time = time.time()
    rsa.set_n(n)
    rsa.set_e(e)
    ciphertext = rsa.encrypt_plaintext(plaintext)
    end_time = time.time()

    return Result(ciphertext=ciphertext), end_time - start_time

def decrypt(rsa: RSA, ciphertext, n, d):
    start_time = time.time()
    rsa.set_n(n)
    rsa.set_d(d)
    plaintext = rsa.decrypt_ciphertext(ciphertext)
    end_time = time.time()

    return Result(plaintext=plaintext), end_time - start_time