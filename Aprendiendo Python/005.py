# Ejercicio basico donde se calculará la propina


# 1) le digo al usuario que ingrese el valor total de la factura
totalFactura = int(input("Ingrese el valor total de la factura: "));

# 2) Pedirle al usuario el valor que quiere dar de propina

valorPropina = int(input("Ingrese el porcentaje que desea dar de propina: "));

# 3) hacer el calculo de la propina

propina = (totalFactura * valorPropina) / 100

# 4) Mostrar al usuario el valor de la propina

print(f"El valor de la propina es de: {propina} pesos")