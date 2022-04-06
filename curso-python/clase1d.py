suma = 0
promedio = 0
contador = 1

while contador <= 3:
    nota = float(input("Ingrese la nota "+ str(contador)+ ": "))
    if nota >= 1.0 and nota <= 7.0:
        suma = suma + nota
        contador = contador + 1

promedio = suma / 3
print("El promedio obtenido es: ", promedio)