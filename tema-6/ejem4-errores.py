try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError as e:
    print("¡Error! Debes introducir un número válido.")
    print(e)
except ZeroDivisionError as e:
    print("¡Error! No puedes dividir entre cero.")
    print(e)
else:
    print("Gracias por proporcionar un número válido!!")

#####################################33

def establecer_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print(f"Edad establecida en {edad}")

try:
    establecer_edad(-5)
except ValueError as e:
    print(f"Capturamos un error personalizado: {e}")