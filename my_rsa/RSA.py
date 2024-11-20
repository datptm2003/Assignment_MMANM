import my_rsa.utils as utils
from config import DEFAULT_KEY_BITS

class RSA():
    def __init__(self):
        self._p = None
        self._q = None
        self._n = None
        self._phi = None
        self._e = None
        self._d = None

    ################### Getter/Setter ###################

    @property
    def p(self):
        if self._p is None:
            self._p = utils.random_prime_with_n_bits(DEFAULT_KEY_BITS // 2)
        return self._p

    @property
    def q(self):
        if self._q is None:
            self._q = utils.random_prime_with_n_bits(DEFAULT_KEY_BITS // 2)
        return self._q

    @property
    def n(self):
        if self._n is None:
            self._n = self.p * self.q
        return self._n
    
    @property
    def phi(self):
        if self._phi is None:
            self._phi = (self.p - 1) * (self.q - 1)
        return self._phi

    @property
    def e(self):
        if self._e is None:
            while True:
                e = utils.random_prime_with_n_bits(utils.size_in_bits(self.phi) // 2)
                if utils.gcd(e, self.phi) == 1:
                    self._e = e
                    break
        return self._e
    
    @property
    def d(self):
        if self._d is None:
            self._d = utils.inverse(self.e, self.phi)
        return self._d
    
    def set_p(self, p):
        self._p = p

    def set_q(self, q):
        self._q = q

    def set_n(self, n):
        self._n = n

    def set_phi(self, phi):
        self._phi = phi

    def set_e(self, e):
        self._e = e

    def set_d(self, d):
        self._d = d

    def reset(self):
        self._p = None
        self._q = None
        self._n = None
        self._phi = None
        self._e = None
        self._d = None

    ################### Support methods ###################

    def encrypt(self, m):
        return utils.power(m, self.e, self.n)

    def decrypt(self, c):
        return utils.power(c, self.d, self.n)
    
    def encrypt_plaintext(self, plaintext):
        if type(plaintext) is str:
            plaintext = plaintext.encode()
            m = utils.bytes_to_long(plaintext)
        # return utils.long_to_bytes(self.encrypt(m))
        print(f"::{m}")
        return self.encrypt(m)

    def decrypt_ciphertext(self, c):
        # if type(ciphertext) is str:
        #     ciphertext = ciphertext.encode()
        # c = utils.bytes_to_long(ciphertext)
        print(f"::{self.decrypt(c)}")
        decrypted_in_bytes = utils.long_to_bytes(self.decrypt(c))
        return decrypted_in_bytes.decode()
    
def __call__():
    return RSA()