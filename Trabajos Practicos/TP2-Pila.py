from pila import Pila


###### Trabajo Practio Pila ##############


#########################################
######### Ejercicio 19 ##################
#########################################

'''
Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, 
desarrollar las funciones necesarias para resolver las siguientes actividades:
a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.
'''
class Movie():
    def __init__(self,title,studio,date):
        self.title = title
        self.studio = studio
        self.date = date

pila = Pila()

movies = [Movie("El señor de los anillos","Warner","2008"),
Movie("Harry Potter","Warner","2018"),
Movie("Matanga dijo la changa","Marvel Studios","2014"),
Movie("Warner picturies pelicula","Warner","2018"),
Movie("Pelicula marvel 1","Marvel Studios","2016"),
Movie("Pelicula marvel 2","Marvel Studios","2018"),
Movie("Wall-e","Pixar","2014"),
Movie("Los increibles","Pixar","2008"),
]


for movie in movies:
    pila.apilar(movie)

movie2014 = []
contador2018 = 0
movieMarvel2016 = []

while not pila.pila_vacia():
    movie =  pila.desapilar()
    if(movie.date == "2014"):
       movie2014.append(movie.title)
    if(movie.date == "2018"):
        contador2018 += 1
    if(movie.date == "2016") and (movie.studio == "Marvel Studios"):
        movieMarvel2016.append(movie)

print("Peliculas de 2014: ")
for movie in movie2014:
    print("-",movie)

print("Cantidad de peliculas en 2018: ")
print("-",contador2018)

print("Peliculas de Marvel Studio estrenadas en 2016:")
for movie in movieMarvel2016:
    print("-",movie.title,movie.studio,movie.date)



'''
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de 
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones 
necesarias para resolver las siguientes actividades:
a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;

b. determinar los personajes que participaron en más de 5 películas de la saga,
 además indicar la cantidad de películas en la que aparece;

c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

d. mostrar todos los personajes cuyos nombre empiezan con C, D y G
'''
print("*************")
print("*************")
print("Ejercicio 24 ")
print("*************")
print("*************")

class Character():
    def __init__(self,name,countMovies):
        self.name = name
        self.countMovies = countMovies

characters = [
    Character("Spider-Man",4),
    Character("Iron Man",8),
    Character("Capitan America",7),
    Character("Black Widow",7),
    Character("Rocket Raccoon",5),
    Character("Groot",3),
    Character("DeadPool",1),
]

chars = ["C","D","G"]

pilaCharacters = Pila()

for character in characters:
    pilaCharacters.apilar(character)

pos = 1
counter = 0
characterFive = []
characterChars = []

while not pilaCharacters.pila_vacia():
    character = pilaCharacters.desapilar()
    if(character.name == "Groot" ) or (character.name == "Rocket Raccoon"):
        print("La posicion de ",character.name,"es :",pos)
    if(character.countMovies > 5):
        characterFive.append(character)
    if(character.name == "Black Widow"):
        print("Black Widow participo en ",character.countMovies,"peliculas")
    if(character.name[0] in chars):
        characterChars.append(character)
    pos += 1

    
print("Los personajes que participaron en mas de 5 sagas son los siguientes:")
for character in characterFive:
    print(character.name,"trabajo en ",character.countMovies)

print("Los personaes que empiezan con letra D, G o C son :")
for character in characterChars:
    print(character.name)
