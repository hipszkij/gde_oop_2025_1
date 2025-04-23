class Car:
    def __init__(self, make, model):
        self._make = make  # _make attribútum, belső használatra
        self._model = model  # _model attribútum, belső használatra

    def get_make(self):
        print("get_make called")
        return self._make

    def set_make(self, make):
        print("set_make called")
        if make:
            self._make = make

    make = property(get_make, set_make)


# Példa használat:
car = Car("Toyota", "Corolla")
print(car.make)

car.make = "valami"
print(car.make)



