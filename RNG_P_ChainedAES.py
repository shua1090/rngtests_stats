from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from RNG import RNG
BLOCK_SIZE = 32

class RNG_AES(RNG):
    def internal_gen(self):
        key = self.key
        while True:
            key = self.internal_cipher.encrypt(pad(key, BLOCK_SIZE))
            yield int.from_bytes(key, byteorder='little') % 256

    def __init__(self,seed):
        self.key = seed
        self.internal_cipher = AES.new(self.key, AES.MODE_ECB)
        self.internal_rng = self.internal_gen()
        pass

    def getNext(self):
        while True:
            yield next(self.internal_rng)
    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn

if __name__ == "__main__":
    key = b'\0'*16
    aes = RNG_AES( key )
    for i in aes.getNextN(100):
        print(i)