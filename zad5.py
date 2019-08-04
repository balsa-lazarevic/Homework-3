lista_original = [
    {"country": "GB",
     "spent": 100
     },
    {"country": "RU",
     "spent": 200
     },
]

lista = []

for zemlja in lista_original:
    nova_zemlja = {}
    nova_zemlja[zemlja["country"]] = zemlja["spent"]
    lista.append(nova_zemlja)

print(lista)