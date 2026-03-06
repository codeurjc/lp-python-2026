class Animal:
    def __init__(self, name):
        self._name = name

    def comer(self):
        print(f"Soy {self._name} y estoy comiendo")

class Dog(Animal):
    def __init__(self, name, breed):
        self._breed = breed
        super().__init__(name)

    def comer(self):
        super().comer()
        print(f"Como {self._breed}")

d = Dog("Vega", "Pienso")
d.comer()