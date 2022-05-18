# ciclo For   

nombres = ["juan", "daniela", "sandra", "andres"];

for i in nombres:
    print(i);
    
    
    
# encontrar el dato mas pequeño de una lista de numeros

numbers = [3,4,6,7,9,78,9, 10];
numero = numbers[0];
for i in numbers:
    if i < numero:
        numero = i


print(f"El numero mas chico de la lista es: {numero}") 


# imprimir el indice y el valor de cada elemento del array

for index, element in enumerate(numbers):
    print(f"El indice es: {index}, y el elemenro de esa posición es: {element}")