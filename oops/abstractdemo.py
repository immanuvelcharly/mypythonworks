from abc import ABC,abstractmethod
class ide(ABC):
    @abstractmethod
    def debug(self):
        pass

class pycharm(ide):
    def debug(self):
        print("pycharm debug method")

class Eclipse(ide):
    def debug(self):
        print("Eclipse debug method")

obj=Eclipse()
obj.debug()


