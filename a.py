class Parent:
    def __init__(self,age,name):
        self.name=name
        self.age=age
        print("This is parent init function")

    def display(self):
        print("Your name is ",self.name," and age is  ",self.age)

class Kid(Parent):
    def __init__(self, age, name,height):
        self.height=height
        super().__init__(age,name)


obkid=Kid(10,"Vihaan",144)
obkid.display()
        