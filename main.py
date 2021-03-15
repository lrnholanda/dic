favorite_languages = {
    'lorena': 'python',
    'chris': 'java',
    'italo': 'c',
    'julia': 'julia'
}

friends = ['chris', 'italo']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
       

# print keys

comidas = {
    'lore': 'pizza',
    'chirs': 'lasanha',
    'italo': 'cu',
}

for name in comidas.keys():
    print(name.title())

# keys and values

comidas = {
    'lore': 'pizza',
    'chirs': 'lasanha',
    'italo': 'cu',
}

print("\nComidas Favoritas")

for name, comida in comidas.items():
    print(f"\n{name.title()}, {comida.title()}")

print(comidas['lore'])