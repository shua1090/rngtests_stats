from RNG import RNG
import subprocess

class RNG_ur(RNG):
    def __init__(self):
        self.internal_rng = self.internal_gen()
        pass

    def internal_gen(self):
        while True:
            result = subprocess.Popen("./urandom/a.out 1", shell=True)
            text = result.communicate()[0]
            return_code = result.returncode
            yield return_code

    def getNext(self):
        while True:
            yield next(self.internal_rng)
    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn