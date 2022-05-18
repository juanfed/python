# imprimir los 5 primeros numeros de una lista

numbers = [85,1,2,3,4,5,6,7,8,9,10,11,12];
contador = 0;
numero = int(input("Ingrese la cantidad de numeros a mostrar: "));

while contador < numero:
    print(numbers[contador]);
    contador = contador + 1;
    
    
print("ciclo for")
for i in range(numero):
    
    print(numbers[i]);