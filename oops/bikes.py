from abc import ABC,abstractmethod
class Bike(ABC):
    name:str
    model:int
    ful_type:str
    def __init__(self,name,model,ful_type):
        self.name=name
        self.model=model
        self.ful_type=ful_type

    @abstractmethod
    def start(self):
        pass
class Ather(Bike):
    def __init__(self, name, model, ful_type):
        super().__init__(name, model, ful_type)

    def start(self):
        print(f"{self.name}starting model{self.model}fuel{self.ful_type}")

at=Ather("aether", 2023,"ev")
at.start()

