from Base.observer import Observer

class Subject: 
    def __init__(self):
        self.__observers = []

    def attach_observer(self, observer: Observer):
        self.__observers.append(observer)

    def detach_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify_observers(self, arg: object):
        for observer in self.__observers:
            observer.notify(arg)