from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self, subject):
        self._subject = subject

    @abstractmethod
    def notify(arg: object):
        pass