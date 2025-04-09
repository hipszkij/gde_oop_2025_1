class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self,message):
        print(f"{message}")



dog = Dog('Bodri')

dog.bark('vau1')

Dog.bark(dog,'vau2')
