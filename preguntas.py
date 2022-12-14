"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    archivo = open('data.csv')

    archivo = archivo.readlines()

    elementosC2 = [int(archivo[i][2]) for i in range(len(archivo))]

    sumatoria = sum(elementosC2)

    return  sumatoria


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    archivo = open('data.csv')

    archivo = archivo.readlines()

    elementos = [archivo[i][0] for i in range(len(archivo))]

    respuesta = [(elementos[i],elementos.count(elementos[i])) for i in range(len(elementos))]

    respuesta = sorted(set(respuesta))
    return  respuesta


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    
    archivo = open("data.csv")

    archivo = archivo.readlines()

    elementos = sorted(set([archivo[i][0] for i in range(len(archivo))]))

    for i in range(len(elementos)):
        sumatoria = 0
        for j in range(len(archivo)):
            if(archivo[j][0] == elementos[i]):
                sumatoria += int(archivo[j][2])
        elementos[i] = (elementos[i],sumatoria)
    return elementos


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    
    archivo = open('data.csv')

    archivo = archivo.readlines()

    elementos = [archivo[i][9:11] for i in range(len(archivo))]

    respuesta = [(elementos[i],elementos.count(elementos[i])) for i in range(len(elementos))]

    respuesta = sorted(set(respuesta))
    
    return respuesta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    archivo = open('data.csv')

    archivo = archivo.readlines()

    elementos = sorted(set([archivo[i][0] for i in range(len(archivo))]))

    for i in range(len(elementos)):
        menor = 100000
        mayor = 0
        for j in range(len(archivo)):
            if(archivo[j][0] == elementos[i]):
                if(int(archivo[j][2]) < menor):
                    menor = int(archivo[j][2])
                elif (int(archivo[j][2]) > mayor):
                    mayor = int(archivo[j][2])
        elementos[i] = (elementos[i],mayor,menor)
    return elementos


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    archivo = open('data.csv')

    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n")[0:-1] for i in range(len(archivo))][:-1]   #Partición por saltos de línea
    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: x.split("\t")[4],elementos))                         #Extrae únicamente elementos del diccionario
    elementos = list(map(lambda x: x.split(","),elementos))                             #El texto de diccionario lo parte por comas
    elementos = [elementos[i][j] for i in (range(len(elementos))) for j in (range(len(elementos[i])))]
    elementos = list(map(lambda x: x.split(":"),elementos))

    elementosSD = []

    for i in range(len(elementos)):
        elementosSD.append(elementos[i][0])

    elementosSD = sorted(list(set(elementosSD)))

    for i in range(len(elementosSD)):
        minimo = 100000
        maximo = 0
        for j in range(len(elementos)):
            if(elementos[j][0]==elementosSD[i]):
                if(minimo > int(elementos[j][1])):
                    minimo = int(elementos[j][1])
                if(maximo < int(elementos[j][1])):
                    maximo = int(elementos[j][1])
        elementosSD[i] = (elementosSD[i],minimo,maximo)

    return elementosSD


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    archivo = open('data.csv')                                                                #Lectura
    
    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n") for i in range(len(archivo))][:-1]         #Partición por saltos de línea
    elementos.append([str(archivo[-1]),''])

    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: x.split("\t")[0:2],elementos))                         #Extrae únicamente elementos del diccionario

    elementosSD = []

    for i in range(len(elementos)):                                                     #Crea lista con todas las claves
        elementosSD.append(int(elementos[i][1]))

    elementosSD = sorted(list(set(elementosSD)))                                        #Elimina duplicados y ordena las claves

    for i in range(len(elementosSD)):
        lista = []
        for j in range(len(elementos)):
            if(int(elementos[j][1])==elementosSD[i]):
                lista.append(elementos[j][0])
        elementosSD[i] = (elementosSD[i],lista)
  
    return elementosSD


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    archivo = open('data.csv')
    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n") for i in range(len(archivo))][:-1]         #Partición por saltos de línea
    elementos.append([str(archivo[-1]),''])

    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: x.split("\t")[0:2],elementos))                         #Extrae únicamente elementos del diccionario

    elementosSD = []

    for i in range(len(elementos)):                                                     #Crea lista con todas las claves
        elementosSD.append(int(elementos[i][1]))

    elementosSD = sorted(list(set(elementosSD)))                                        #Elimina duplicados y ordena las claves

    for i in range(len(elementosSD)):
        lista = []
        for j in range(len(elementos)):
            if(int(elementos[j][1])==elementosSD[i]):
                lista.append(elementos[j][0])
        lista = sorted(list(set(lista)))
        elementosSD[i] = (elementosSD[i],lista)
    return elementosSD


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    archivo = open('data.csv')
    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n")[0:-1] for i in range(len(archivo))][:-1]   #Partición por saltos de línea
    elementos.append([str(archivo[-1]),''])
    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: x.split("\t")[4],elementos))                         #Extrae únicamente elementos del diccionario
    elementos = list(map(lambda x: x.split(","),elementos))                             #El texto de diccionario lo parte por comas
    elementos = [elementos[i][j] for i in (range(len(elementos))) for j in (range(len(elementos[i])))]
    elementos = list(map(lambda x: x.split(":"),elementos))
    elementos = list(map(lambda x: x[0],elementos))
    elementosSD = sorted(list(set(elementos)))
    elementosSD = dict([(elementosSD[i],elementos.count(elementosSD[i])) for i in range(len(elementosSD))])
    return elementosSD


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    archivo = open('data.csv')                                                                #Lectura

    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n")[0:-1] for i in range(len(archivo))][:-1]   #Partición por saltos de línea
    elementos.append([str(archivo[-1]),''])
    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: [x.split("\t")[0],x.split("\t")[3],x.split("\t")[4]],elementos))                         #Extrae únicamente elementos del diccionario
    elementos = list(map(lambda x: [x[0],x[1].split(","),x[2].split(",")],elementos))
    elementos = list(map(lambda x: (x[0],len(x[1]),len(x[2])),elementos))
    
    return elementos


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    archivo = open('data.csv')                                                                #Lectura

    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n")[0:-1] for i in range(len(archivo))][:-1]   #Partición por saltos de línea y limpieza
    elementos.append([str(archivo[-1]),''])
    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: [int(x.split("\t")[1]),x.split("\t")[3]],elementos))      #Extrae únicamente elementos del diccionario
    elementos = list(map(lambda x: [x[0],x[1].split(",")],elementos))

    for i in range(len(elementos)):
        fila = [elementos[i][0]]
        for j in range(len(elementos[i][1])):
            fila.append(elementos[i][1][j])
        elementos[i] = fila

    elementosSD = []

    for i in range(len(elementos)):
        for j in range(1,len(elementos[i])):
            elementosSD.append(elementos[i][j])
    elementosSD = sorted(list(set(elementosSD)))

    for i in range(len(elementosSD)):
        sumatoria = 0
        for j in range(len(elementos)):
            if(elementosSD[i] in elementos[j]):
                sumatoria += elementos[j][0]
        elementosSD[i] = (elementosSD[i],sumatoria)
    elementosSD = dict(elementosSD)
    return elementosSD


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    archivo = open('data.csv')                                                                #Lectura

    archivo = archivo.readlines()

    elementos = [str(archivo[i]).split("\n")[0:-1] for i in range(len(archivo))][:-1]   #Partición por saltos de línea y limpieza
    elementos.append([str(archivo[-1]),''])
    elementos = list(map(lambda x: x[0], elementos))                                    #En cada posición de la lista grande queda el texto y no la lista
    elementos = list(map(lambda x: [x.split("\t")[0],x.split("\t")[4]],elementos))      #Extrae únicamente elementos del diccionario
    elementos = list(map(lambda x: [x[0],x[1].split(",")],elementos))

    for i in range(len(elementos)):
        fila = [elementos[i][0]]
        for j in range(len(elementos[i][1])):
            fila.append(int(elementos[i][1][j][elementos[i][1][j].find(":")+1:]))
        elementos[i] = fila

    elementosSD = [elementos[i][0] for i in range(len(elementos))]
    elementosSD = sorted(list(set(elementosSD)))

    for i in range(len(elementosSD)):
        sumatoria = 0
        for j in range(len(elementos)):
            if(elementosSD[i] in elementos[j]):
                sumatoria += sum(elementos[j][1:])
        elementosSD[i] = (elementosSD[i],sumatoria)
    elementosSD = dict(elementosSD)
    return elementosSD
