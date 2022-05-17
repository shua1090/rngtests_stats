from RNG import RNG
import subprocess

import jpype as jp
class RNG_Java_Random(RNG):
    def __init__(self):
        jp.startJVM(jp.getDefaultJVMPath(), "-ea")
        self.internal_java_rng = jp.java.util.Random()
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
