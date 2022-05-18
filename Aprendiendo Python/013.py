# ejercicio con condicional

# En una llantería se ha establecido una promoción de las llantas marca «Ponchadas», dicha promoción consiste en lo siguiente:

# Si se compran menos de cinco llantas el precio es de $30000 cada una, de $25000 si se compran de cinco a 10 y de $20000 si se compran más de 10.
# Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compra y la que tiene que pagar por el total de la compra.

cantidadLlantas = int(input("Ingrese la cantidad de llantas que va a comprar: "));

if cantidadLlantas <= 0:
    print("No se puede realizar su compra porque a introducido un cero o un numero negativo ")
elif cantidadLlantas >= 1 and cantidadLlantas <= 5:
    print(f"El el total por comprar {cantidadLlantas} llantas es de: {cantidadLlantas * 30000}");
    print("el preio por cada llanda es de 30.000 pesos")
elif cantidadLlantas > 5 and cantidadLlantas <= 10:
    print(f"El el total por comprar {cantidadLlantas} llantas es de: {cantidadLlantas * 25000}");
    print(f"El precio por cada llanda es de: {(cantidadLlantas * 25000) / cantidadLlantas}");
elif cantidadLlantas > 10:
    print(f"El el total por comprar {cantidadLlantas} llantas es de: {cantidadLlantas * 20000}");
    print(f"El precio por cada llanda es de: {(cantidadLlantas * 20000) / cantidadLlantas}");