##  ---------------Recursividad------------------- ##


## Las funciones recursivas deben tener una variable de control 
## que se actualize dentro de la funcion recursiva.

## Las funciones recursivas se llaman a si mismas.

## Ejemplo con factorial de un numero:
## el factorial de 5! = 5 * 4! ( 5 por el factorial de 4).

def factorial(num):
    if(num == 0):
        return 1
    else:
        return num * factorial(num-1)


print(factorial(10))

##