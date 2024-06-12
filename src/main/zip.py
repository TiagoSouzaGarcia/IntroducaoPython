objeto_zip = zip([1,2,3], ['Adamastor', 'Caio', "Flavio"])

print(list(objeto_zip))

id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

mapa = list(zip(id, regiao))
print(mapa)

codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["maçã", "uva", "banana", "laranja"]

mercadorias = list(zip(codigos, frutas))
print(mercadorias)

tupla_iteravel = [('J392', 'João'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claúdia'), ('A49', 'Ana')]
print(tupla_iteravel)
ids, nomes  = zip(*tupla_iteravel)

ids = list(ids)
nomes = list(nomes)

print("IDs = ", ids)
print("Nomes = ", nomes)

alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)
