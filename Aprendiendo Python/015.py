# calcular el precio de una compra dependiendo de la cantidad de huevos y arepas que el cliente vaya a comprar.

# precio base de los huevos = 1800
# precio base de las arepas = 5000

#NOTA: Si alguien compra mas de 10 canastas, el precio será de 1000

# si alguien compra mas de 10 canastas de huevos y ademas compra 10 paquetes de arepas, el precio de los huevos sera de 1000 y el de las arepas de 2000


# paso 1

cantHuevos = int(input("Ingrese la cantidad de huevos a comprar: "));
opcion = int(input("Ingrese 1 si va a comprar arepas o 2 si no va a comprar arepas: "));

if opcion == 1 :
    cantArepas = int(input("Ingrese la cantidad de arepas que quiere comprar: "));
    if cantHuevos > 10 and cantArepas > 10 :
        print("El valor de cada huevo es de: 1000 pesos")
        print("El valor de cada arepa es de: 1000 pesos")
        print(f"El valor total de compra es de: {(cantHuevos * 1000) + (cantArepas * 2000)} pesos");
    elif cantHuevos > 10 :
        print("El valor de cada huevo es de: 1000 pesos")
        print("El valor de cada arepa es de: 2000 pesos")
        print(f"El valor total es de: {(cantHuevos * 1000) + (cantArepas * 2000)} pesos")
    else:
        print("El valor de cada huevo es de: 1800 pesos")
        print("El valor de cada arepa es de: 2000 pesos")
        print(f"El valor total es de: {(cantHuevos * 2000) + (cantArepas * 2000)} pesos")
elif cantHuevos > 10 :
    print("El valor de cada huevo es de: 1000 pesos")
    print(f"El valor total es de: {cantHuevos * 1800} pesos");
else:
    print("El valor de cada huevo es de: 1800 pesos")
    print(f"El valor total de la compra es de: {cantHuevos * 1800} pesos")