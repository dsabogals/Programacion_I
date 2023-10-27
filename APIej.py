import requests

url="https://rickandmortyapi.com/api/character"

characters=requests.get(url).json()
response=requests.get(url)

if (response.status_code == 200):

#Numero de personajes:
    print("El total de personajes es: ", characters["info"]["count"])

#Informacion de personajes:
    i=1
    for character in characters["results"]:
        print(i, ". " , "Nombre:", character["name"], " Estado:", character["status"], " Especie:", character["species"])
        i+=1

#Genero:
    female=[]
    male=[]
    for character in characters["results"]:
        if (character["gender"]=="Male"):
            male.append(character)
        else:
            female.append(character)
    print("Cantidad de hombres:", len(male))
    print("Cantidad de mujeres:", len(female))

#Especies:
    species=[]
    species_contador=[]
    for character in characters["results"]:
        if(character["species"] not in species):
            species.append(character["species"])
    
    for specie in species:
        count=0
        for character in characters["results"]:
            if (character["species"] == specie):
                count += 1
        species_contador.append(count)
    print(species)
    print(species_contador)
    print("Humanos:", species_contador[0], "Aliens:", species_contador[1])

#Top 5:
    character_episode=[]
    for character in characters["results"]:
        character_episode.append([len(character["episode"]), character["name"]])
    
    character_episode.sort(key=lambda x: x[0], reverse=True)
    print(character_episode[:5])
    