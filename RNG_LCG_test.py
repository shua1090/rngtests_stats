def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

from RNG import RNG
import subprocess

class RNG_LCG(RNG):
    def __init__(self, modulus, a, c, seed):
        self.internal_rng = lcg(modulus, a, c, seed)
        pass

    def getNext(self):
        while True:
            yield next(self.internal_rng)
    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn