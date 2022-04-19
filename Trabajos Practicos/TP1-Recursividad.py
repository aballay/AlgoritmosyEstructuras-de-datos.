## Ejercicios 5-22-23

###########################################
##############  Ejercicio 5 ###############
###########################################
# I:1
# v:5
# x:10
# l:50
# c:100
# d:500
# m:1000

# - Se leen de izq a derecha y se suman sus valores.
# - Cuando se coloca un simbolo de valor menor, a la izquierda de otro, se resta.


# - Se permiten tres repeticiones del mismo simbolo .
# - El simbolo : 
# 	I solo se resta con V-X
#   x solo se resta con L-C
#  	C solo se resta ocn D-M


romans = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

def ConvertToDecimal(nRomano,acumulador = 0):
    if(len(nRomano) > 1):
        if(romans.get(nRomano[0]) >= romans.get(nRomano[1])):
            acumulador = acumulador + romans.get(nRomano[0])
            return ConvertToDecimal(nRomano[1:len(nRomano)],acumulador)
        else:
            acumulador = acumulador - romans.get(nRomano[0])
            return ConvertToDecimal(nRomano[1:len(nRomano)],acumulador)
    elif(len(nRomano)==1):
       return  acumulador + romans.get(nRomano[0])
    else:
        return acumulador

# Se debe ingresar un numero romano valido si no hara cualquier cosa 

num = "MMMCCXXIV"
res = ConvertToDecimal(num)
print("nuermo romano",num)
print("numero a decimal",res)



###########################################
############## Ejercicio 22 ###############
###########################################
'''
El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos 
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con 
ayuda de la fuerza” realizar las siguientes actividades:

a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no 
queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
c. Utilizar un vector para representar la mochila

Aplicar busqueda recursiva
'''

bag = ["petaca de ginebra","Sable de luz","Botas de cuero","reljo de arena","Gafas","Celular","Puñal","Barra de chocolate"]

#Defino busqueda secuencial
def busquedaSecuencial(vector,buscado):
    if(len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector) - 1
    else:
        print("Se encontro",vector[-1],"en la mochila.")
        return busquedaSecuencial(vector[:-1],buscado)



busquedaObjetos = busquedaSecuencial(bag,"Sable de luz")
if(busquedaObjetos != -1):
    print("Se encontro el sable de luz")
    print("Se tuvieron que sacar",len(bag)-busquedaObjetos,"objetos de la mochila para encontrarlo")
else:
    print("No se encontro el sable de luz en la mochila que contiene ",len(bag),"objetos")

############################################
############### Ejercicio 23 ###############
############################################
'''
Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una 
matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal– 
y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0) 
y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda 
avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo
'''

def Labyrinth(matrix, x=0, y=0, out = []):
    #verifica que no este fuera de la matriz
    if (x >= 0) and (x <= len(matrix) - 1) and (y >= 0) and (y <= len(matrix[0]) - 1):
        ## verifica si esta en la salida del laberinto
        if (x == len(matrix) - 1) and (y == len(matrix[0]) - 1): 
            out.append([x, y])
            print("Se ha encontrado la salida del laberinto. Usando el siguiente camino")
            print(out)
        # Verifica si existe un camino posible
        elif (matrix[x][y] == 1):
            out.append([x,y])
            #marca que el camino ya fue recorrido
            matrix[x][y] = 'x'
            # avanza una posicion para cada casillero.
            Labyrinth(matrix, x, y + 1, out)
            Labyrinth(matrix, x, y - 1, out)
            Labyrinth(matrix, x + 1, y, out)
            Labyrinth(matrix, x - 1, y, out)
    # el laberinto no tiene salida
    if ([len(matrix) -1, len(matrix[0]) - 1]) not in out:
        return False

lab  =     [[1, 1, 1, 1, 1, 0],
                 [1, 0, 0, 0, 1, 1],
                 [1, 1, 1, 1, 0, 1], 
                 [0, 0, 0, 1, 0, 1],
                 [0, 0, 1, 1, 0, 1],
                 [0, 0, 0, 0, 0, 1]]


resultado = Labyrinth(lab)
if (resultado == False):
    print("El laberinto no tiene salida :c")
else:
    print("wipi")