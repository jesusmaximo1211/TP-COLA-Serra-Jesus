Queue=[{"nombre":"Luke SkayWalker", "planeta":"Tatooine"},
    {"nombre": "Han Solo", "planeta": "Corellia"},
    {"nombre": "Leia Organa", "planeta": "Alderaan"},
    {"nombre": "Yoda", "planeta": "Dagobah"},
    {"nombre": "Chewbacca", "planeta": "Kashyyyk"},
    {"nombre": "Darth Vader", "planeta": "Tatooine"},
    {"nombre": "Jar Jar Binks", "planeta": "Naboo"},
    {"nombre": "C-3PO", "planeta": "Tatooine"} ]
    
#a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
def dedondeson(queue,planetas):
    personajesenplanetas=[]
    for personaje in queue:
        if personaje["planeta"] in planetas:
            personajesenplanetas.append(personaje["nombre"])
    return personajesenplanetas
planetas=["Alderaan","Endor","Tatooine"]
personajess=dedondeson(Queue, planetas)
print("LOS PERSONAJES DE LOS PLANETAS ALDERAAN ENDOR O TATOOINE SON :" ,personajess)

#b indicar el planeta natal de luke skayewalkjer y han solo
def planeta_natal(Queue,natal):
    personajenatalidad={}
    for personaje in Queue:
        if personaje["nombre"] in natal:
            personajenatalidad[personaje["nombre"]]= personaje ["planeta"]
    return personajenatalidad
natal=["Luke SkayWalker","Han Solo"]
natales=planeta_natal(Queue,natal)
print("EL PLANETA NATAL DE LUKE SKAYALKER Y HAN SOLO SON: ", natales)

#c agregar uno mas adelante de yoda
def antesdeyoda(Queue, nuevo_personaje):
    nueva_cola = []
    for personaje in Queue:
        if personaje["nombre"] == "Yoda":
            nueva_cola.append(nuevo_personaje)
        nueva_cola.append(personaje)
    return nueva_cola

nuevo_personaje = {"nombre": "Obi-Wan Kenobi", "planeta": "Stewjon"}
personajes = antesdeyoda(Queue, nuevo_personaje)
for personaje in personajes:
    print(f"Nombre: {personaje['nombre']}, Planeta: {personaje['planeta']}")

#d eliminar el personaje ubicado despues de Jar Jar Binks
Queue.pop(7)
print (Queue)