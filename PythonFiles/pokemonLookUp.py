input = open(pokemon.txt, 'r')
pokemon = []

for line in input:
    pokemon.append(line.rstrip('\n'))
input.close()

for i in pokemon:
    print(i)

allPokemon = {'Bulbasaur':{'index':1,'types':['Grass','Poison'],'stats':{'hp':45,'atk':49,'def':49,'spa':65,'spd':65,'spe':45}},
'Venusaur':{'index':2,'types':['Grass','Poison'],'stats':{'hp':60,'atk':62,'def':63,'spa':80,'spd':80,'spe':60}}
}
