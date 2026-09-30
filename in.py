class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name," is ",self.age)
class child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)