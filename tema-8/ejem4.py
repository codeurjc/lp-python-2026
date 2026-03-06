class Animal:
    def __init__(self, name):
        self._name = name

    def comer(self):
        print("Estoy comiendo")

class Dog(Animal):
    def comunicar(self):
        print(f"Guau! Soy {self._name}")

class Cat(Animal):
    def comer(self):
        print("Dame de lo que me gusta!!!")

    def comunicar(self):
        print(f"Miau! Soy {self._name}")

d = Dog("Vega")
c = Cat("Minino")

d.comer()
c.comer()

d.comunicar()
c.comunicar()

d.dormir()

d.owner