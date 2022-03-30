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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")
Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor
Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
pala_1= str(input("Ingrese la 1er palabra: "))
pala_2= str(input("Ingrese la 2da palabra: "))
pala_3= str(input("Ingrese la 3ra palabra: "))

print("Seleccione una opción de ordenamiento")
print("1.- Ordenar por orden alfabético (usando el operador >)")
print("2.- Ordenar por cantidad de letras (longitud de la palabra (len) y operador >)")
seleccion=int(input("Selección: "))

pala_1= pala_1.upper()
pala_2= pala_2.upper()
pala_3= pala_3.upper()


if seleccion == 1:
    print("ORDEN ALFABETICO")
    if pala_1 > pala_2: 
        if pala_1 > pala_3:
            if pala_2 > pala_3:
                print(pala_1,pala_2,pala_3)
            else:
                print(pala_1,pala_3,pala_2)
        else:
            print(pala_3,pala_1,pala_2)
    else:
        if pala_2 > pala_3:
            if pala_1 > pala_3:
                print(pala_2,pala_1,pala_3)
            else:
                print(pala_2,pala_3,pala_1)
        else:
            if pala_1 > pala_2:
                print(pala_3, pala_1,pala_2)
            else:
                print(pala_3,pala_2,pala_1)
elif seleccion == 2:
        print("ORDENAR POR CANTIDAD DE LETRAS")
        if len(pala_1) > len(pala_2): 
            if len(pala_1) > len(pala_3):
                if len(pala_2) > len(pala_3):
                    print(pala_1,pala_2,pala_3)
                else:
                    print(pala_1,pala_3,pala_2)
            else:
                print(pala_3,pala_1,pala_2)
        else:
            if len(pala_2) > len(pala_3):
                if len(pala_1) > len(pala_3):
                    print(pala_2,pala_1,pala_3)
                else:
                    print(pala_2,pala_3,pala_1)
            else:
                if len(pala_1) > len(pala_2):
                    print(pala_3, pala_1,pala_2)
                else:
                    print(pala_3,pala_2,pala_1)
else:
    print("OPCIÓN INCORRECTA - FIN DEL PROGRAMA")