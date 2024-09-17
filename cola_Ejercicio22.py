personajes = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"},
    {"personaje": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
]

#a determinar el nombre del personajes de la superheroe capitana marvel;

def nomcapmarvel(personajes):
    for personaje in personajes:
        if personaje["superheroe"]=="Capitana Marvel":
            return personaje["personaje"]
            
nombre_superheroe=nomcapmarvel(personajes)
print ("a) EL NOMBRE DE LA CAPITANA MARVEL ES",nombre_superheroe)

#b mostrar nombres de personajes femeninos

def femeninos(personajes):
    superheroesfemeninos=[]
    for personaje in personajes:
        if personaje["genero"]=="F":
            superheroesfemeninos.append (personaje["superheroe"])
    return superheroesfemeninos
pfemenino= femeninos(personajes)
print ("B) LOS PERSONAES FEMENINOS SON ", pfemenino)

#c ostrar los nombres de los personajes masculinos
def masculinos(personajes):
    superheroesmasculinos=[]
    for personaje in personajes:
        if personaje["genero"]=="M":
            superheroesmasculinos.append(personaje["superheroe"])
    return superheroesmasculinos
pmasculino=masculinos(personajes)
print ("C) LOS PERSONAJES MASCULINOS SON: ", pmasculino)

#d determinar le nombre de scort lang
def suplang (personajes):
    for personaje in personajes:
        if personaje["personaje"]=="Scott Lang":
            return personaje["superheroe"]
    
superheroescott= suplang(personajes)
print ("D) EL NOMBRE DE SUPERHEROE DE SCOTT LANG ES: ",superheroescott)

#e mostrar datos de supererohes cuyos nombres qwue empiezan con S

def inicials(personajes):
    personajesqueempiezancons=[]
    for personaje in personajes:
        if personaje["personaje"].startswith("S"):
            personajesqueempiezancons.append(personaje)
    return personajesqueempiezancons
inicialcons=inicials(personajes)
print("e) los personajes que empiezan con S son",inicialcons)

#f Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe

def carol (personajes):
    for personaje in personajes:
        if personaje["personaje"]=="Carol Danvers":
            return personaje["superheroe"]

caroldanver=carol(personajes)
print("F) CAROL DANVER SE ENCUENTRA, Y SU SUPERHEROE ES; ",caroldanver)



