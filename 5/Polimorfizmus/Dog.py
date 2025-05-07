from Animal import Animal


class Dog(Animal):
    def __init__(self, name, type, age):
        super().__init__(name, type)
        self.age = age

