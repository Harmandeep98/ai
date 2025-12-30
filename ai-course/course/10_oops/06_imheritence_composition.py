class BaseChai:
    def __init__(self, type_):
        self.type= type_

    def preparing (self):
        print(f"preparing tea{self.type} chai...............")    

class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding spices for {self.type} tea")


#composition in classes

class Chaishop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")
        
    def serve(self):
        print(f"Serving {self.chai.type}")
        self.chai.preparing()

class FancyChai(Chaishop):
    chai_cls = MasalaChai

