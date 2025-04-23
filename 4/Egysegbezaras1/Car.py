class Car:
    def __init__(self, make, model):
        self._make = make  # _make attribútum, belső használatra
        self._model = model  # _model attribútum, belső használatra

    def get_make(self):
        return self._make

    def set_make(self, make):
        if make:
            self._make = make


# Példa használat:
car = Car("Toyota", "Corolla")
print(car.get_make())

car.set_make("valami")
print(car.get_make())



