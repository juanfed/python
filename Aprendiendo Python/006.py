# ejercicio basico parecido al archivo 005.py pero un poco mas largo

# 1: pedir el total de la factura

valorFactura = int(input("Ingrese el valor de la factura: "));

# 2: Pedir el porcentaje de propina que se quiere dar

valorPropina = int(input("Ingrese el porcentaje de la propina que quiere dar"));

# 3: Calcular el valor del IVA del 19%

iva = (valorFactura * 0.19)

# 4: Calcular el subtotal (total de la factura - valor del iva)

subtotal = valorFactura - iva;

# 5: Calcular el valor de la propina (subtotal * propina / 100) 

valorPropina = (subtotal * valorPropina) / 100

# 6: Mostrar el resultado
valorTotal = valorFactura + valorPropina
print(f"El iva fué de: {iva} pesos")
print(f"El valor propina fué de: {valorPropina} pesos")
print(f"El subtotal fué de: {subtotal} pesos")
print(f"El valor total de la factura mas la propina es de: {valorTotal} pesos")