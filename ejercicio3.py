class GrafoDeLocalidades:
    def __init__(self, grafo):
        self.grafo = grafo

    def es_conexo(self):
        visitados = set()
        
        # Búsqueda en profundidad (DFS)
        def dfs(nodo):
            visitados.add(nodo)
            for vecino, _ in self.grafo[nodo]:
                if vecino not in visitados:
                    dfs(vecino)

        # Comenzamos desde cualquier nodo (ej. el primero en el diccionario)
        inicio = next(iter(self.grafo))
        dfs(inicio)

        # Verificamos si visitamos todos los nodos
        return len(visitados) == len(self.grafo)

# Grafo de localidades
localidades = {
    "Madrid": [("Alcorcón", 13), ("Villaviciosa de Odón", 22), ("Alcalá de Henares", 35)],
    "Villanueva de la Cañada": [("Villaviciosa de Odón", 11), ("Boadilla del Monte", 7)],
    "Alcorcón": [("Madrid", 13), ("Móstoles", 5)],
    "Móstoles": [("Alcorcón", 5), ("Fuenlabrada", 8)],
    "Fuenlabrada": [("Móstoles", 8), ("Getafe", 10)],
    "Getafe": [("Fuenlabrada", 8), ("Madrid", 16)],
    "Villaviciosa de Odón": [("Madrid", 22), ("Villanueva de la Cañada", 11)],
    "Boadilla del Monte": [("Villanueva de la Cañada", 7), ("Madrid", 15)],
    "Alcalá de Henares": [("Madrid", 35), ("Torrejón de Ardoz", 15)],
    "Torrejón de Ardoz": [("Alcalá de Henares", 15), ("Madrid", 20)]
}

# Crear una instancia de GrafoDeLocalidades
grafo = GrafoDeLocalidades(localidades)

# Verificar si el grafo es conexo
es_conexo = grafo.es_conexo()
print("¿El grafo es conexo?:", es_conexo)
