import atexit
from abc import abstractmethod


class Managed:

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


def register_managed(managed):
    managed.start()
    atexit.register(managed.stop)