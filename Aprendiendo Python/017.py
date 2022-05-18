# Mostrar si un estudiante esta habilitado para presentar un examen
# si el estudiante fue a mas del 75% de las clases podrá presentar el examen
#Si el estudiante fué a menos del 75% de las clases, solo puede hacer el examen si tiene excusa medica

# porcentajes de las clases asistidas (100* clasesAsistidas) / numeroClases

numeroClases = int(input("Ingrese la cantidad de clases: "));

clasesAsistidas = int(input("Ingrese la cantidad de clases que asistió: "));

porcentaje = (100 * clasesAsistidas) / numeroClases


if porcentaje >= 75 :
    print("El estudiante puede presentar el examen");
elif porcentaje < 75:
    excusa = int(input("Ingrese 1 si tiene excusa medica ó 2 si no tiene excusa medica: "));
    if excusa == 1:
        print("Puede presentar el examen")
    else:
        print("La persona no puede presentar el examen");


