from tasklist import (
    random_prime_task, gcd_task, find_d_task, find_keys_task,
    encrypt_task, decrypt_task
)

list_of_tasks = [
    random_prime_task, 
    gcd_task, 
    find_d_task, 
    find_keys_task, 
    encrypt_task, 
    decrypt_task
]

print_str = \
"""                                Welcome to our RSA system!!!
----------------------------------------------------------------------------------------------------
    0. Exit
    1. Find a large prime number given the desired number of bits for the prime.
    2. Calculate the greatest common divisor (GCD) of two large integers.
    3. Compute the decryption key d given the encryption key e and two large prime numbers p and q.
    4. Generate a random key pair given two large prime numbers p and q.
    5. Encrypt a message (in string) given the message and the encryption key e and n.
    6. Decrypt a ciphertext (in number) given the encrypted message and the decryption key d and n.
-----------------------------------------------------------------------------------------------------"""
print(print_str)

while True:
    try:
        num = int(input("Choose your option >: "))
    except ValueError:
        print("Invalid input! Option must be of type int.")
        print("-----------------------------------------------------------------------------------------------------")
        continue
    if num < 0 or num > 6:
        print("Invalid input! Option must be in range [0, 6].")
        print("-----------------------------------------------------------------------------------------------------")
        continue
        
    if num == 0:
        print("Thank you and good bye!")
        break
    else:
        list_of_tasks[num-1].perform()
        print("-----------------------------------------------------------------------------------------------------")
        input("Press Enter to continue.")
        print("-----------------------------------------------------------------------------------------------------")
        