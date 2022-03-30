# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperaturas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temp_1=int(input("Ingrese la 1er temperatura:"))
temp_2=int(input("Ingrese la 2da temperatura:"))
temp_3=int(input("Ingrese la 3ra temperatura:"))

# Determinación de la temperatura máxima
if temp_1 > temp_2:
    if temp_1 > temp_3:
        print("La temperatura MÁXIMA es {}".format(temp_1))
    else:
        print("La temperatura MÁXIMA es {}".format(temp_3))
else:
    if temp_2 > temp_3:
        print("La temperatura MÁXIMA es {}".format(temp_2))
    else:
        print("La temperatura MÁXIMA es {}".format(temp_3))

# Determinación de la temperatura mínima
if temp_1 < temp_2:
    if temp_1 < temp_3:
        print("La temperatura MÍNIMA es {}".format(temp_1))
    else:
        print("La temperatura MÍNIMA es {}".format(temp_3))
else:
    if temp_2 < temp_3:
        print("La temperatura MÍNIMA es {}".format(temp_2))
    else:
        print("La temperatura MÍNIMA es {}".format(temp_3))

# Determinación de la temperatura promedio
temp_prom= (temp_1 + temp_2 + temp_3) / 3
print("Las temperaturas registradas fueron {} {} {}".format(temp_1,temp_2,temp_3))
print("La temperatura promedio fue de: {}".format(temp_prom))
