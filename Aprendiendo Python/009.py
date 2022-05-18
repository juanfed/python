# Ejercicio donde se calculará el IMC (indice de masa corporal)

# 1: pedir la estatura y el peso de la persona

estatura = int(input("Ingrese su estatura en centimetros: "));
peso = int(input("Ingrese su peso corporal en kilogramos: "));

# 2: convierto la estatura de centmetro a metros

altura = estatura / 100;

# 3: Calculo su IMC

IMC = peso / (altura ** 2);

# 4: Mostrar el resultado de su indice de masa corpporal
print(f"Su indice de masa corporal es de: {IMC} kg/m2")

if IMC < 18.5:
    print("Tiene un peso muy inferior");
if IMC >= 18.5 and IMC < 24.9:
    print("Su peso es normal");
if IMC >= 25 and IMC <= 29:
    print("Tiene un peso algo por encima de lo normal");
if IMC > 30:
    print("Tiene sobrepeso");