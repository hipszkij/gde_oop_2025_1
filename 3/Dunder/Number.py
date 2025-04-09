class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Szám értéke: {self.value}"

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            return Number(self.value + other)  # Más típusokkal is működjön, ha szükséges

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        else:
            return Number(self.value - other)  # Más típusokkal is működjön, ha szükséges

number1 = Number(1)
number2 = Number(5)

print(number1)  # Kiírja: Szám értéke: 1


number6 = number2 + number1
print(number6)  # Kiírja: Szám értéke: 5


number4 = number2 - number1
print(number4)