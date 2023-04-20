import json
lista = {0:"lapiz", "2":"borrador", "3":"cuaderno", "4":"lapicero"}
with open("lista.json", "w") as archivo: json.dump(lista, archivo)
archivo.close()

with open('lista.json', 'r') as f:
  data = json.load(f)
print(data["3"])