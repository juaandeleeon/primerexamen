import heapq
# Uso el algoritmo de Dijkstra ya que es ideal para encontrar la ruta más corta en términos de
# distancia cuando las aristas del grafo tienen diferentes pesos.
def ruta_mas_corta_dijkstra(grafo, inicio, destino):
    # Inicialización
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    previos = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == destino:
            break

        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    # Reconstrucción del camino
    camino = []
    nodo = destino
    while nodo is not None:
        camino.append(nodo)
        nodo = previos[nodo]
    camino = camino[::-1]

    # Resultado
    if distancias[destino] < float('inf'):
        print(f"Ruta más corta de {inicio} a {destino}: {' -> '.join(camino)}")
        print(f"Distancia total: {distancias[destino]} km")
    else:
        print(f"No hay ruta desde {inicio} hasta {destino}")

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

# Solicitar localidades de inicio y destino al usuario
inicio = input("Ingrese la localidad de origen: ")
destino = input("Ingrese la localidad de destino: ")

# Verificar que las localidades existan en el grafo
if inicio in localidades and destino in localidades:
    ruta_mas_corta_dijkstra(localidades, inicio, destino)
else:
    print("Una o ambas localidades no existen en el grafo.")
