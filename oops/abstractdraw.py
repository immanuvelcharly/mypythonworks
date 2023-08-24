from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class rectangle(shape):
    def draw(self):
        print("draw rectangle")

class triangle(shape):
    def draw(self):
        print("draw triangle")

obj=rectangle()
obj.draw()

