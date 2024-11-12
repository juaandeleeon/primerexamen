from collections import deque

class GrafoDeLocalidades:
    def __init__(self, grafo):
        self.grafo = grafo

    def rutas_alternativas(self, inicio, destino):
        # Cola para almacenar las rutas parciales (ruta, distancia acumulada)
        cola = deque([([inicio], 0)])  # Comienza con la ruta que solo tiene el inicio y la distancia 0
        rutas = []

        while cola:
            # Extraemos la primera ruta de la cola
            ruta, distancia_acumulada = cola.popleft()
            nodo_actual = ruta[-1]

            # Si llegamos al destino, añadimos la ruta y la distancia total a las rutas encontradas
            if nodo_actual == destino:
                rutas.append((ruta, distancia_acumulada))
            else:
                # Exploramos cada vecino no visitado en la ruta actual
                for vecino, distancia in self.grafo.get(nodo_actual, []):
                    if vecino not in ruta:  # Evitamos pasar dos veces por la misma localidad
                        nueva_ruta = list(ruta)
                        nueva_ruta.append(vecino)
                        cola.append((nueva_ruta, distancia_acumulada + distancia))

        # Imprimimos todas las rutas encontradas
        if rutas:
            print(f"Rutas de {inicio} a {destino}:")
            for i, (ruta, distancia) in enumerate(rutas, 1):
                print(f"Ruta {i}: {' -> '.join(ruta)} | Distancia total: {distancia} km")
        else:
            print(f"No se encontraron rutas de {inicio} a {destino}.")

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

# Solicitar al usuario las localidades de origen y destino
inicio = input("Ingrese la localidad de origen: ")
destino = input("Ingrese la localidad de destino: ")

# Llamar al método para encontrar las rutas alternativas
grafo.rutas_alternativas(inicio, destino)
