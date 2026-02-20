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

