# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de números, utilizar "for"
# para recorrer toda la lista y realizar la sumatoria de todos los números
# La sumatoria se deberá ir guardando en la variable "suma"
numeros = [1, 5, -1, 6, 10, 2, -5]
suma = 0   # Variable ya inicializada, la suma arranca en cero
for num in numeros:
    suma= suma + num
print("La suma de los números es: ",suma)

#INTENTANDO HACERLO DE OTRA FORMA
suma = 0   # Variable ya inicializada, la suma arranca en cero
for i in range(len(numeros)):
    suma= suma + numeros[i]
print("La suma de los números es: ",suma)

#SUMANDO LOS ELEMENTOS DE LA LISTA USANDO LA FUNCION SUM
suma = 0
suma = sum(numeros)
print("La suma de los numeros es: ",suma)
print("terminamos!, el resultado final almacenado en suma debe ser 18")
