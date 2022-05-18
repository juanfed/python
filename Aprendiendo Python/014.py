# programa que me dice si un numero ingresado es mayor, menor o si ese numero corresponde con el numero a hallar.

number = 72

numberIngresado = int(input("Ingrese un número: "));

if number > numberIngresado :
    print(f"El número ingresado es menor al número que se quiere hallar");
elif number < numberIngresado:
    print("El número ingresado es mayor al número que se quiere hallar")
else :
    print(f"Su número ${numberIngresado} corresponde al número a encontrar, felicidades")