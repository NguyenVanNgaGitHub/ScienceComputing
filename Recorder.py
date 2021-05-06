from abc import ABC, abstractmethod

class Recorder(ABC):
    def __init__(self, dla = None):
        self.dla = dla

    @abstractmethod
    def record(self):
        return NotImplementedError

    @abstractmethod
    def export_result(self):
        return NotImplementedError