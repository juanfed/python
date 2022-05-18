# for con listas dentro de listas(matrices)

matriz = [[1,2,3], [9,8,7], [4,5,6,7,8], 1,2,3,4,5,6,5,6,7,8,9];

for fila in matriz:
    print(fila);
    for element in fila:
        print(element)