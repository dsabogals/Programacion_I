import requests

url = "https://rickandmortyapi.com/api/character/"
response = requests.get(url)

# 1. Cantidad de personajes

if response.status_code == 200:
    data = response.json()
    personajes = data["results"]
    total_personajes = data["info"]["count"]
    print("1. Total de personajes: ", total_personajes)

# 2. Imprimir la información de cada personaje
print("2. Informacion de los personajes: ")
for personaje in personajes:
        print(f"{personaje['name']} - {personaje['status']} - {personaje['species']}")

# 3. Agrupar por género y calcular la respectiva cantidad

contar_genero = {}
print("3. Numero de personajes por género: ")
for personaje in personajes:
    genero = personaje["gender"]
    if genero in contar_genero:
        contar_genero[genero] += 1
    else:
        contar_genero[genero] = 1

for genero, count in contar_genero.items():
    print(f"{genero}: {count}")

# 4. Agrupar por especies y calcular la respectiva cantidad

contar_especies = {}
print("4. Cantidad de personajes por especie:")
for personaje in personajes:
    especies = personaje["species"]
    if especies in contar_especies:
        contar_especies[especies] += 1
    else:
        contar_especies[especies] = 1  
for especies, count in contar_especies.items():
    print(f"{especies}: {count}")

# 5. Los 5 personajes con más apariciones

aparicion_personajes = sorted(personajes, key=lambda x: len(x["episode"]), reverse=True)
top_5_personajes = aparicion_personajes[:5]
print("5. Los 5 personajes con más apariciones:")
for personaje in top_5_personajes:
    print(f"{personaje['name']} - Apariciones: {len(personaje['episode'])}")


