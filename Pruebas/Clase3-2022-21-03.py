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

## Sucecion de fibonacci 
## 0 1 1 2 3 5 8 13 21 ... etc
## fb5 = fb(5-2) + fb(5-1)

def fibonacci(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fibonacci(num-1)  + fibonacci(num-2) 

print(fibonacci(10))

