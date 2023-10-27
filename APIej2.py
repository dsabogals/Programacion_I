import json
import matplotlib.pyplot as plt

a=open('futurama.json')
characters=json.load(a)

#1. Agrupar en listas por género a los personajes.

female=[]
male=[]
others=[]
for character in characters:
    if character["gender"]=="Female":
        female.append(character)
    elif character["gender"]=="Male":
        male.append(character)
    else:
        others.append(character)

#2. A partir de las especies que aparecen en las listas construidas en el punto anterior, haga el respectivo diagrama de barras de especies. 
print("Especies por genero femenino")
species_female_type={}
for species in female:
    specie = species["species"]
    if specie in species_female_type:
        species_female_type[specie]+=1
    else:
        species_female_type[specie] = 1

for specie, count in species_female_type.items():
    print(f"Specie: {specie}, Count: {count}")
print("Especies por genero masculino")
species_male_type={}
for species in male:
    specie=species["species"]
    if specie in species_male_type:
        species_male_type[specie]+=1
    else:
        species_male_type[specie]=1

for specie, count in species_male_type.items():
    print(specie, count)

plt.bar(species_male_type.keys(), species_male_type.values(), color='#ABE4F9', label='Masculino')
plt.bar(species_female_type.keys(), species_female_type.values(), color='#F6C2F9', label='Femenino')
plt.xlabel('Especies')
plt.ylabel('Numero de especies')
plt.title('Total de especies por genero')
plt.legend()
plt.show()

#3. Haga un diagrama de sectores (pie, torta .....) de las especies sin la agrupación por género. 
print("Total de especies")
total_species={}
for character in characters:
    specie=character["species"]
    if specie in total_species:
        total_species[specie]+=1
    else:
        total_species[specie]=1
for specie, count in total_species.items():
    print(specie, count)

plt.pie(total_species.values(), labels=total_species.keys())
plt.title("Distribución de Especies")
plt.show()

#4. Hacer un histograma de las edades por listado de géneros
print("Edades por genero femenino")
age_female={}
for age in female:
    ages=int(age["age"])
    if ages in age_female:
        age_female[ages]+=1
    else:
        age_female[ages]=1
for ages, count in age_female.items():
    print(f"Age: {ages}, Count: {count}")

print("Edades por genero masculino")
age_male={}
for age in male:
    ages=(age["age"])
    if ages in age_male:
        age_male[ages]+=1
    else:
        age_male[ages]=1
for ages, count in age_male.items():
    print(f"Age: {ages}, Count: {count}")

plt.hist(age_female.values(), bins=range(min(age_female.keys()), max(age_female.keys())+20, 5))
plt.title('Edades por genero femenino')

#5. Haga un histograma de las edades sin la agrupación por género. 

print("Total de edades")
total_ages={}
for character in characters:
    ages=character["age"]
    if ages in total_ages:
        total_ages[ages]+=1
    else:
        total_ages[ages]=1
for age, count in total_ages.items():
    print(f"Age: {age}, Count: {count}")

#6. Agrupar los nombres completos de los personajes en una lista e imprimirla (Hagan uso del desarollo del punto 1)
print("Nombres completos:")
full_name=[]
for character in female:
    full_name.append(character['name']['first']+" "+character['name']['middle']+" "+character['name']['last'])
for character in male:
    full_name.append(character['name']['first']+" "+character['name']['middle']+" "+character['name']['last'])
print(full_name)