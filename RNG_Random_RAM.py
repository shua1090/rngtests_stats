# Get ram used at any given moment and modulus it
import psutil
class RNG_ur(RNG):
    def __init__(self):
        self.internal_rng = self.internal_gen()
        pass

    def internal_gen(self):
        while True:
            yield psutil.virtual_memory().free % 256

    def getNext(self):
        while True:
            yield next(self.internal_rng)
    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn
