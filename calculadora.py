#Calculadora

operador= input("Que operacion quieres realizar? (+,-,*,/): ")

valorUno= int(input("Ingresa el primer numero: "))
valorDos= int(input("Ingresa el segundo numero: "))

resultado=None

if operador == "+":
    resultado= valorUno + valorDos
elif operador == "-":
    resultado= valorUno - valorDos
elif operador == "*":
    resultado= valorUno * valorDos
elif operador == "/":
    if valorDos == 0: #Evitar dividir por cero
        print("No es posible dividir por cero")
    else:
        resultado= valorUno / valorDos
else:
    print("Algo salio mal")

if resultado is not None:
    print(f"El resultado es {resultado}")


