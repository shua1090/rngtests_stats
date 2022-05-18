

class RNG_Middle_Square(RNG):
    def __init__(self,seed):
        self.number = seed
        self.internal_rng = internal_gen()
        pass
    
    def internal_gen(self):
        while True:
            self.number = int(str(self.number*self.number).zfill(8)[2:6])
            yield self.number % 255

    def getNext(self):
        while True:
            yield next(self.internal_rng)
    def getNextN(self, n):
        nextn = []
        for i in range(n):
            nextn.append(next(self.internal_rng))
        return nextn