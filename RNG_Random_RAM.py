# Get ram used at any given moment and modulus it
from RNG import RNG
import psutil
import time
class RNG_RAM(RNG):
    def __init__(self):
        self.internal_rng = self.internal_gen()
        pass

    def internal_gen(self):
        while True:
            a = psutil.virtual_memory().used
            time.sleep(0.001)            
            yield a % 1000 % 256

    def getNext(self):
        while True:
            yield next(self.internal_rng)
    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn
