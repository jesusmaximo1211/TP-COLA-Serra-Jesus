#pag 196 del libro
import heapq

class Operacion:
    def __init__(self, prioridad, encargado, descripcion, hora, stormtroopers=None):
        self.prioridad = prioridad 
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.stormtroopers = stormtroopers

    def __lt__(self, other):
        return self.prioridad < other.prioridad

    def __repr__(self):
        stormtroopers_str = f", Stormtroopers: {self.stormtroopers}" if self.stormtroopers else ""
        return f"[Prioridad: {self.prioridad}] Encargado: {self.encargado}, Descripción: {self.descripcion}, Hora: {self.hora}{stormtroopers_str}"


cola_prioridad = []

operaciones = [
    Operacion(3, "Snoke", "Revisión de sistemas", "10:00"),
    Operacion(3, "Kylo Ren", "Entrenamiento con sable de luz", "10:30"),
    Operacion(2, "Capitán Phasma", "Inspección de escuadrón", "11:00"),
    Operacion(2, "Capitán Phasma", "Entrenamiento de tropas", "11:30"),
    Operacion(2, "Capitán Phasma", "Mantenimiento de equipo", "12:00"),
    Operacion(2, "Capitán Phasma", "Revisión de seguridad", "12:30"),
    Operacion(1, "General Hux", "Informe de actividades", "13:00"),
    Operacion(1, "General Hux", "Planificación de ataque", "13:30"),
    Operacion(1, "General Hux", "Supervisión de recursos", "14:00"),
    Operacion(1, "General Hux", "Control de comunicaciones", "14:30")
]


for operacion in operaciones:
    heapq.heappush(cola_prioridad, operacion)

def atender_operaciones(cola, cantidad_atender):
    for i in range(cantidad_atender):
        if cola:
            operacion = heapq.heappop(cola)
            print(f"Atendiendo: {operacion}")
        else:
            print("No hay más operaciones")
        
        if i == 4:
            print("\nAgregando operación solicitada por Capitán Phasma...\n")
            nueva_operacion = Operacion(2, "Capitán Phasma", "Revisión de intrusos en el hangar B7", "15:00", stormtroopers=25)
            heapq.heappush(cola, nueva_operacion)
        if i == 5:
            print("\nAgregando operación solicitada por Líder Supremo Snoke...\n")
            nueva_operacion = Operacion(3, "Snoke", "Destrucción del planeta Takodana", "15:30")
            heapq.heappush(cola, nueva_operacion)


print("Atendiendo operaciones de la cola de prioridad:")
atender_operaciones(cola_prioridad, 8) 
