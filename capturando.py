import csv

def leer_csv(nombre_archivo):
    lista_pokemons = []
    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            lista_pokemons.append(fila)
    return lista_pokemons

pokemons = leer_csv('pokemons.csv')
