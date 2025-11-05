try:
    entero = int(input("Ingrese un n´pumero: "))
    print(entero)

except ValueError:
    print("El valor ingresado no es un número")
else:
    print("La operacion se realizo correptamente")
    print(entero)
finally:
    print("Pudes continuar con el programa")
