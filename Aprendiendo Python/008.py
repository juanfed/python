# ejercicio de convercion de grados a  fahrenheit y viceverza 

# 1: saber si ingresara en grados o en  fahrenheit

opcion = int(input("Ingrese 1 para convertir de grados centigrados fahrenheit o cualquier otra tecla para el proceso inverso: "));

valor = int(input("Ingrese el valor que desea convertir: "));
# 2: realizar la convercion segun el caso
if(opcion == 1):
    fahrenheit = (valor * 9/5) + 32; 
    print(f"{opcion} Grados centigrados es igual a: {fahrenheit} grados fahrenheit");
else: 
    grados = (valor - 32) * 5/9;
    print(f"{opcion} Grados fahrenheit es igual a: {grados} grados centigrados");
