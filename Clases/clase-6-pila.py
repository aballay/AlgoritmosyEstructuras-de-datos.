from pila import Pila
from random import randint

pila = Pila()
pilaAux = Pila()
pilaInit = Pila()

palabra = "abcddcba"

for i in palabra:
    pila.apilar(i)
    pilaInit.apilar(i)


while(not pila.pila_vacia()):
    pilaAux.apilar(pila.desapilar())

while((not pilaInit.pila_vacia()) and (pilaInit.cima() == pilaAux.cima())):
    pilaInit.desapilar()
    pilaAux.desapilar()

if(pilaInit.pila_vacia()):
    print("Palabra palindromo")
else:
    print("Palabra no palindroma")
# Invertir cadena
# Ejercicio pila


## ejercicio 11
pila11 = Pila()

words = "abcdefguaaoff"
vocals = ["a","e","i","o","u"]

for x in words:
    pila11.apilar(x)

counter = 0
while(not pila11.pila_vacia()):
    if(pila11.desapilar() in vocals):
        counter+=1

print("cantidad de vocales",counter)



## ejercicio 13

class Trajes():
    def __init__(self,traje,pelicula,estado,resenia = ""):
        self.__traje = traje
        self.__pelicula = pelicula
        self.__estado = estado
        self.resenia = resenia
    
    def getTraje(self):
        return self.__traje
    def getPelicula(self):
        return self.__pelicula
    def getEstado(self):
        return self.__estado


traje1 = Trajes("mark I","Marvel I", "Excelente")
traje2 = Trajes("mark II","Marvel II", "Regular")
traje3 = Trajes("Mark III","Marvel III","Pobre")

pPila = Pila()

pPila.apilar(traje1)
pPila.apilar(traje2)
pPila.apilar(traje3)

print(pPila.cima().getTraje())



