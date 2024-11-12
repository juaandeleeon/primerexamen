class GrafoDeLocalidades:
    def __init__(self, grafo):
        self.grafo = grafo

    def ruta_mas_larga(self, inicio, destino):
        # Llamada inicial a la función recursiva para encontrar la ruta más larga
        ruta, distancia = self._ruta_mas_larga_dfs(inicio, destino, set())
        if ruta:
            print(f"Ruta más larga de {inicio} a {destino}: {' -> '.join(ruta)}")
            print(f"Distancia total: {distancia} km")
        else:
            print(f"No hay ruta válida de {inicio} a {destino}.")

    def _ruta_mas_larga_dfs(self, nodo_actual, destino, visitados):
        # Caso base: Si llegamos al destino, devolvemos la ruta actual y distancia 0
        if nodo_actual == destino:
            return [nodo_actual], 0

        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)
        ruta_mas_larga = None
        distancia_mas_larga = -1

        # Exploramos cada vecino del nodo actual
        for vecino, distancia in self.grafo.get(nodo_actual, []):
            if vecino not in visitados:
                # Llamada recursiva para continuar la búsqueda desde el vecino
                ruta, distancia_acumulada = self._ruta_mas_larga_dfs(vecino, destino, visitados)
                
                # Si encontramos una ruta, actualizamos la más larga si es mayor
                if ruta:
                    distancia_total = distancia + distancia_acumulada
                    if distancia_total > distancia_mas_larga:
                        ruta_mas_larga = [nodo_actual] + ruta
                        distancia_mas_larga = distancia_total

        # Desmarcar el nodo actual al retroceder
        visitados.remove(nodo_actual)
        return ruta_mas_larga, distancia_mas_larga

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

# Solicitar al usuario las localidades de inicio y destino
inicio = input("Ingrese la localidad de origen: ")
destino = input("Ingrese la localidad de destino: ")

# Llamar al método para encontrar la ruta más larga
grafo.ruta_mas_larga(inicio, destino)
