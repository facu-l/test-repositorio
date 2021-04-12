nombres ='''
'Agustin',
'Alan',
'Andrés',
'Ariadna',
'Bautista',
'CAROLINA',
'CESAR',
'David',
'Diego',
'Dolores',
'DYLAN',
'ELIANA',
'Emanuel', 
'Fabián',
'Facundo',
'Facundo',
'FEDERICO',
'FEDERICO',
'GONZALO',
'Gregorio',
'Ignacio',
'Jonathan',
'Jonathan',
'Jorge',
'JOSE',
'JUAN',
'Juan',
'Juan',
'Julian',
'Julieta',
'LAUTARO',
'Leonel',
'LUIS',
'Luis',
'Marcos',
'María',
'MATEO',
'Matias',
'Nicolás',
'NICOLÁS',
'Noelia',
'Pablo',
'Priscila',
'TOMAS',
'Tomás',
'Ulises',
'Yanina'
'''

eval1= '''
81,
60,
72,
24,
15,
91,
12,
70,
29,
42,
16,
3,
35,
67,
10,
57,
11,
69,
12,
77,
13,
86,
48,
65,
51,
41,
87,
43,
10,
87,
91,
15,
44,
85,
73,
37,
42,
95,
18,
7,
74,
60,
9,
65,
93,
63,
74
'''
eval2= '''
30,
95,
28,
84,
84,
43,
66,
51,
4,
11,
58,
10,
13,
34,
96,
71,
86,
37,
64,
13,
8,
87,
14,
14,
49,
27,
55,
69,
77,
59,
57,
40,
96,
24,
30,
73,
95,
19,
47,
15,
31,
39,
15,
74,
33,
57,
10
'''

nombres = nombres.split(',')
eval1 = eval1.split(',')
eval2 = eval2.split(',')
notaFinal = []           #guardaremos la nota final
for nota1, nota2 in zip(eval1,eval2):
    notaFinal.append(sum([int(nota1),int(nota2)]))

def promedio():
    # Saca promedio sum() obtiene la suma de las notas finales dadas, y len(list) devuelve la longitud de la lista por nombres.
    return sum(notaFinal)/len(nombres)

def reporte(l):
    """ Leemos un dos numeros: minimo y maximo, nos aseguramos que maximo
      sea mayor a minimo y usamos ese rango para imprimir en pantalla
      a todos los alumnos que estan dentro de el
    """
    minimo = int(input("Ingrese el menor posible: "))
    maximo = int(input("Ingrese el mayor posible: "))
    if(maximo > minimo): 
        i = 0
        for num in l:
            if(minimo < int(num)) and (maximo > int(num)):
                print(f"el alumno {nombres[i].strip()} esta dentro del rango")
            i = i + 1
    else: 
        print("Error en el ingreso del rango")

def imprimir (nombres,eval1,eval2,notaFinal):
    """ Guardamos una lista donde va a estar ordenada segun el criterio
      que haya elegido el usuario

      opcion 1: ordenada de menor a mayor por nombres
      opcion 2: ordenada de menor a mayor por eval1
      opcion 3: ordenada de menor a mayor por eval2
      opcion 4: ordenada de menor a mayor por notaFinal
    """
    opcion_ordenar = input("Ingrese por que orden quiere ordenar (nombres,eval1,eval2,notaFinal): ").lower()
    while not(opcion_ordenar in ["nombres","eval1","eval2","notafinal"]):
        print("No se ingreso una opcion valida")
        opcion_ordenar = input("Ingrese por que orden quiere ordenar (nombres,eval1, eval2, notaFinal): ").lower()
    # guardaremos los datos ordenados
    listaOrdenada = list(zip(nombres,eval1,eval2,notaFinal))
    if(opcion_ordenar == "nombres"):
        listaAux = sorted(listaOrdenada, key=lambda nombres : nombres)
        print(listaAux)
    elif(opcion_ordenar == "eval1"):
        listaAux = sorted(listaOrdenada, key=lambda eval1 : eval1[1])
        print(listaAux)
    elif(opcion_ordenar == "eval2"):
        listaAux = sorted(listaOrdenada, key=lambda eval2 : eval2[2])
        print(listaAux)
    elif(opcion_ordenar == "notafinal"):
        listaAux = sorted(listaOrdenada, key=lambda notaFinal : notaFinal[3])
        print(listaAux)
    return listaAux

print("Menu de lxs estudiantes")
print("1: informara el promedio")
print("2: hara un reporte")
print("3: ordenara los datos")

opcion = int(input("Ingrese un valor : "))
if type(opcion)!=int or opcion not in range(1,4):
    while type(opcion)!=int or opcion not in range(1,4):
        print("No se ingreso una opcion valida, por favor intente nuevamente")
        opcion = int(input("Ingrese un valor : "))

if (opcion == 1):
  print(f"El promedio es: {promedio()}")

if (opcion == 2):
    opcion_reporte = input("Ingrese que quiere reportar (eval1, eval2, notaFinal): ").lower()
    while not(opcion_reporte in ["eval1","eval2","notafinal"]):
       print("No se ingreso una opcion valida")
       opcion_reporte = input("Ingrese que quiere reportar (eval1, eval2, notaFinal): ").lower()
    if(opcion_reporte == "eval1"):
      reporte(eval1)
    if(opcion_reporte == "eval2"): 
      reporte(eval2)
    if(opcion_reporte == "notafinal"):
      reporte(notaFinal)
if(opcion == 3):
    imprimir (nombres,eval1,eval2,notaFinal)