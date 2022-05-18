# sistema de calificaciones: 
# Pedir la calificacion  de un examen con nota de 0 a 5
# 0 - 3 imprimir insuficiente (3 no incluido)
# 3 - 4 imprimir aceptable (4 no incluido)
# 4 - 4.6 imprimir sobresaliente (4.6 no incluido)
# 4.6 - 5 imprimir exelente
# en cualquier otro rango, imprimir "calificación inválida"

nota = float(input("Ingrese la calificación del examen: "));

if nota >= 0 and nota < 3 :
    print("Su calificación es insuficiente")
elif nota >= 3 and nota < 4:
    print("Su califcación es aceptable")
elif nota >= 4 and nota < 4.6:
    print("Su nota es sobresaliente")
elif nota >= 4.6 and nota <= 5:
    print("Su nota ha sido exelente!")
else:
    print("Calificación inválida")