import csv

def leer_csv(nombre_archivo):
    lista_pokemons = []
    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            lista_pokemons.append(fila)
    return lista_pokemons

pokemons = leer_csv('pokemons.csv')

def calcular_valor_total(pokemon):
    ataque = int(pokemon['attack'])
    defensa = int(pokemon['defense'])
    return ataque * defensa

def es_factible(conjunto_pokemons):
    plazo = 0
    for pokemon in conjunto_pokemons:
        plazo += 24
        if plazo < int(pokemon['base_egg_steps']):
            return False
    return True

