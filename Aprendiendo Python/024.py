# ejercico de buscar un elemento
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for i in coleccion:
    if i == 7:
        print(i)
        break
    
contador = 0;
for i in coleccion:
    if i == 7:
        print(f"El númereo se encuentra en la posicion: {contador} de la lista")
        print(i)
        break
    contador = contador + 1