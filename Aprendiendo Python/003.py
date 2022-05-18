# Pido datos a el usuario, pediremos edades y mostraremos la diferencia de edad

# 1) pido la edad al usuario usando el comando input

# con esto muestro mensaeje y capturo lo que usuario ingrese por teclado
edad1 = input("Ingrese la edad de la primera persona: "); # por defecto me los lee como string
edad2 = int(input("Ingrese la edad de la segunda persona: ")); # para evitar convertilo en un entero mas abajo

# 2) calculo la diferencia de edad de ambas personas

diferenciaEdad = int(edad1) - int(edad2); 

# 3) mprimo la diferencia de las edades de las personas
print(f"La diferencia de edad de las dos personas es de: {diferenciaEdad} años")