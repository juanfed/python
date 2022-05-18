# condicionales if else (ejercicios)

# 1: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

number = int(input("Ingrese un numero: "));

if(number <= 0): 
    print("El numero ingresado no hace parte de los numeros enteros");
else:
    if(number == 1):
        print(f"El número {number} es un número impar");
    if(number == 2):
        print(f"El número {number} es un número par");
    if(number % 2 == 0):
        print(f"El número {number} es un numero par");
    if(number % 2 == 1):
        print(f"El número {number} es un numero impar");