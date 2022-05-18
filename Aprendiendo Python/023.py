#diccionarios 

diccionario = {"juan" : 23, "camila" : 16, "andres" : 32, "jessica": 25}

# para imprimir solo los nombres osea la key
for key in diccionario:
    print(key) 
    
# para imprimir llave y valor almacenado en los diccionarios
for key, value in diccionario.items():
    print(f"key: {key}, value: {value}");