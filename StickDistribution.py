from abc import ABC, abstractmethod

import random
class StickDistribution(ABC):
    def __init__(self, dla = None):
        self.dla = dla

    @abstractmethod
    def compute_proba(self, pos : (int,int)) -> float:
        return NotImplementedError

    def can_stick(self, pos : (int,int)) -> float:
        threshold = random.random()
        if threshold <= self.compute_proba(pos):
            return True
        else:
            return False
