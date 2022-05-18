# Ejercio sobre estado de cuentas de una empresa

# pedir ingresos

from traceback import print_tb


ingresos = int(input("Ingrese el total de ingresos de la empresa: "));
# pedir costos

costos = int(input("Ingrese el total de os costos: "));

# calcular utildad bruta (ingresos - costo)

utilidadBruta = ingresos - costos;

# pedir los gastos

gastos = int(input("Ingrese los gastos de la empresa: "));

# calcular la utilidad operativa (utilidad bruta - gastos)

utilidadOperativa = utilidadBruta - gastos;

# calcular el impuesto a la renta (utilidad operativa * 30%)

impuestoRenta = utilidadOperativa * 0.3;

# calcular utilidad neta (utilidad bruta - impuesto a la renta)

utilidadNeta = utilidadOperativa - impuestoRenta;

# mostrar los resultados

print(f"La utlidad bruta de la empresa fue de: {utilidadBruta}");
print("-------------------------------------------------------------------------------------------------------------")
print(f"La utlidad operativa de la empresa fue de: {utilidadOperativa}");
print("-------------------------------------------------------------------------------------------------------------")
print(f"El impuesto a la renta fue de: {impuestoRenta}");
print("-------------------------------------------------------------------------------------------------------------")
print(f"L utilidad neta de la empresa fué de: {utilidadNeta}");
print("-------------------------------------------------------------------------------------------------------------")
print(f"El impuesto de la renta que toca pagar es de: {impuestoRenta}");