from abc import ABC,abstractmethod
class Createview(ABC):
    model:str
    template_name:str
    form_class:str

    def __init__(self,model,template_name,form_class):
        self.model=model
        self.template_name=template_name
        self.form_class=form_class
    @abstractmethod
    def create(self):
        pass
class employeecreate(Createview):
    def __init__(self, model, template_name, form_class):
        super().__init__(model, template_name, form_class)

    def create(self):
        print("founcatnality for creating employee")

emp=employeecreate("employee","employee.html","empform")
emp.create()
    