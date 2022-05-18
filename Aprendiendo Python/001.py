# Forma de hacer los comentario en python
### aca se vera lo basico de las operaciones, uso del print, asignar valores

print("hola mundo"); #forma en la que muestro un dato por patanlla o terminal
print(5+12);


#forma para asignarle a una variable un valor
texto = "como estas"; # uso las commillas para espesificar que es un dato de tipo string 
print(texto);
numero = 5; #forma de asignar un número a una variable
print(numero);
booleano = True;  #forma de asignale un valor de tipo booleano a una varibale
print(booleano);

# un poco mas sobre print
print("primer mensaje", "segundo mensaje", "tercer mensaje"); # forma de tener vaios mensajes

print(f"La suma de 5 mas 12 es: {5 +12}"); # print usando un formato especial para concatener variables

variable1 = 10
variable3 = 30
variable4 = 40

variableSuma = variable4 + variable3 + variable1;
multiplicarVariable = (variable3 * variable4) + variable1; # con los parentesis puedo agrupar las operaciones

print(variableSuma, variable3, multiplicarVariable); # la coma tambien sirve para mostrar varios valores

# puedo sumar texto

texto1 = "hola";
texto2 = "adios"

texto = texto1 + texto2;
print(texto)


# suma textos con numeros

text = "100";
number1 = 852;

# sumaNumero = text + number1;
# print(sumaNumero); # me mostrará un error, para solucionarlo deberia de hacer lo sigueinte

sumaNumero2 = number1 + int(text); # me convertirá el texto en un numero
print(sumaNumero2)
sumaNumero3 = str(number1) + text; # convertira el numero en un texto
print(sumaNumero3);