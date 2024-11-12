class GrafoDeLocalidades:
    def __init__(self, grafo):
        self.grafo = grafo

    def localidades_con_conexiones_cortas(self, max_distancia=15):
        localidades_validas = []
        for localidad, conexiones in self.grafo.items():
            # Verificamos si todas las conexiones tienen una distancia menor a max_distancia
            if all(distancia < max_distancia for _, distancia in conexiones):
                localidades_validas.append(localidad)
        return localidades_validas

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

# Llamar al método para identificar localidades con conexiones cortas
localidades_cortas = grafo.localidades_con_conexiones_cortas()
print("Localidades con todas las conexiones de menos de 15 km:", localidades_cortas)
