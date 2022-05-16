from abc import ABC, abstractmethod

class RNG:
    @abstractmethod
    def __init__(self):
        pass

    # This is a generator
    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def getNextN(self, n):
        pass
