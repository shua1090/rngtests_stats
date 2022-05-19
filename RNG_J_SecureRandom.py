from RNG import RNG
import subprocess

import jpype as jp
class RNG_Java_SecureRandom(RNG):
    def __init__(self):
        jp.startJVM(jp.getDefaultJVMPath(), "-ea")
        self.internal_java_rng = jp.java.security.SecureRandom()
        self.internal_rng = self.internal_gen()
        
        pass
    def close(self):
        jp.shutdownJVM() 

    def internal_gen(self):
        while True:
            yield self.internal_java_rng.nextInt(256)

    def getNext(self):
        while True:
            yield next(self.internal_rng)

    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn

if __name__ == "__main__":
    a = RNG_Java_SecureRandom()
    for i in a.getNextN(50):
        print(i)