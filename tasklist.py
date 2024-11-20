from my_rsa import RSA
from tasks import Task
from tasks.callback import (
    find_random_prime, find_gcd, find_d, find_keys,
    encrypt, decrypt
)

rsa = RSA()

# Task for finding a random prime number with specified bit length
random_prime_task = Task(
    rsa=rsa,
    description="Find a random prime number with a specified number of bits",
    typecasts={
        "n_bits": int
    },
    callback=find_random_prime
)

# Task for finding the greatest common divisor (GCD) of two numbers
gcd_task = Task(
    rsa=rsa,
    description="Find greatest common divisor (GCD) of two large numbers",
    typecasts={
        "a": int,
        "b": int
    },
    callback=find_gcd
)

# Task for finding the private exponent `d` given primes `p`, `q` and public exponent `e`
find_d_task = Task(
    rsa=rsa,
    description="Find the private key exponent (d) given primes p, q, and public exponent e",
    typecasts={
        "p": int,
        "q": int,
        "e": int
    },
    callback=find_d
)

# Task for finding RSA keys (n, e, d) given primes `p` and `q`
find_keys_task = Task(
    rsa=rsa,
    description="Find RSA keys (n, e, d) given two prime numbers p and q",
    typecasts={
        "p": int,
        "q": int
    },
    callback=find_keys
)

# Task for encrypting a plaintext message using public key (n, e)
encrypt_task = Task(
    rsa=rsa,
    description="Encrypt a plaintext message (in string) using public key (n, e)",
    typecasts={
        "plaintext": str,
        "n": int,
        "e": int
    },
    callback=encrypt
)

# Task for decrypting a ciphertext message using private key (n, d)
decrypt_task = Task(
    rsa=rsa,
    description="Decrypt a ciphertext message (in integer) using private key (n, d)",
    typecasts={
        "ciphertext": int,
        "n": int,
        "d": int
    },
    callback=decrypt
)