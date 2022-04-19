
## Sucecion de fibonacci 
## 0 1 1 2 3 5 8 13 21 ... etc
## fb5 = fb(5-2) + fb(5-1)

def fibonacci(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fibonacci(num-1)  + fibonacci(num-2) 

print("fibonacci",fibonacci(5))

## Ejercicio 2 - libro algoritmos y estructuras de datos
## Implementar una función que calcule la suma de todos los números enteros comprendidos
## entre cero y un número entero positivo dado.

## sum10 = 10 + sum9
## sum9 = 9 + sum8
## sum 1 = 1 +sum(0)
0 

def ejercicio2(num):
    if(num == 0):
        return num
    else:
        return num + ejercicio2(num - 1)    

print("sumatoria",ejercicio2(5))


## Ejercicio 3
## Implementar una función para calcular el producto de dos números enteros dados.
# 
# 
#  

# 10 * 7 = 10 + 10 * 6
# 10 * 6 = 10 + 10 * 5
# 10 * 1 = 10 + 10 * 0
# x * y = x + x * y - 1 
  
def producto(x,y):
    if(y == 1):
        return x 
    else:
        return x + producto(x,y-1)

print("producto",producto(5,10))

## Ejercicio 4
# Implementar una función para calcular la potencia dado dos números enteros, el primero re-
# presenta la base y segundo el exponente.
# 10 ^ 8 = 10 * 10 ^ 7
# 10 ^ 7 = 10 * 10 ^ 6
# 10 ^ 1 = 10 * 10   
# x ^ y = x * potencia(x,y -1)
# base , exponente
# 
# base = base * 
# #

def potencia(pBase,pExponente):
    if(pExponente == 1):
        return pBase
    else:
        return pBase * potencia(pBase,pExponente - 1)

print("potencia",potencia(2,5))


## Ejercicio 5 ------------------------
## Desarrollar una función que permita convertir un número romano en un número decimal.
##  I = 1 
##  NO ENTENDI


## Ejercicio 6 ------------------
## Dada una secuencia de caracteres, obtener dicha secuencia invertida.
## cabildo = odlibac
## inverse(palabra)
## -palabra = palabra[len(palabra)]
## palabra = 
def inverse(palabra):
    if(len(palabra) == 1):
        return palabra
    else:
        return  palabra[-1] + inverse(palabra[:-1])

print("Invertir",inverse("ahora"))

### Ejercicio 7 -------------------------
## Desarrolar un algoritmo que permita calcular la siguiente serie
## h(n) = 1 + 1/2 + 1/3 + 1/4 ... + 1/n 

## 1/n = 1/n + sum(1/m-1)

def sumatoriaFraccion(n):
    if(n==1):
        return n
    else:
        return 1/n + sumatoriaFraccion(n-1)

print("Sumatoria Fraccion ",sumatoriaFraccion(5))


## Ejercicio 10
## Desarrollar un algortimo que cuente la cantidad de digitos de un numero entero
##  
## 99 = 1 + 98
def calcDigitos(num):
    if(len(str(num)) == 0):
        return  0
    else:
       return 1 + calcDigitos(str(num)[:-1])
    

print("Calcular cantidad de digitos",calcDigitos(123456789))


## Ejercicio 20 ------------
## Desarrollar un algoritmo que permita implementar la busqueda secuencial con centinela de manera 
## recursiva y permita determinar si esta o no en la lista


def busquedaSecuencial(vector,buscado):
    if(len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector) - 1
    else:
        return busquedaSecuencial(vector[:-1],buscado)

vector = [1,2,3,4,5]

print("busqedaSecuencial",busquedaSecuencial(vector,7))



## Ejercicio X
## Busqueda binaria
## Desarrollar el algoritmo de busqueda binaria de manera recursiva
## El vector debe ser ordenado antes de la busqueda.

vector = [1,2,3,4,5]

def BusquedaBinaria(vector,buscado,primero,ultimo):
    med = (primero + ultimo) // 2
    if(primero > buscado):
        return -1
    if (buscado == vector[med]):
        return med
    elif(vector[med] < buscado):
        return BusquedaBinaria(vector,buscado,med+1,ultimo)
    else:
        return BusquedaBinaria(vector,buscado,primero,med-1)


print("Busqueda binaria :",BusquedaBinaria(vector,4,0,len(vector)-1))



